module OpenAddressHashMap

type OpenAddressHashMap<'Key, 'Value when 'Key: comparison> =
    { MaxSize: int
      Storage: ('Key * 'Value) option array
      Size: int }

let calculateHash (maxSize: int) (key: 'Key) : int =
    (hash key) % maxSize
    |> (fun x -> if x < 0 then x + maxSize else x)

let rec findCell
    (key: 'Key)
    (maxSize: int)
    (storage: ('Key * 'Value) option array)
    (currentIndex: int)
    (probeAmount: int)
    : int option =
    if probeAmount >= maxSize then
        None
    else
        match storage.[currentIndex] with
        | Some (k, _) when k = key -> Some currentIndex
        | None -> Some currentIndex
        | _ -> findCell key maxSize storage ((currentIndex + 1) % maxSize) (probeAmount + 1)

let rec insert (key: 'Key) (value: 'Value) (map: OpenAddressHashMap<'Key, 'Value>) : OpenAddressHashMap<'Key, 'Value> =
    if float map.Size / float map.MaxSize = 1 then
        let newMaxSize = map.MaxSize * 2
        let newStorage = Array.create newMaxSize None

        let newMap =
            { MaxSize = newMaxSize
              Storage = newStorage
              Size = map.Size }

        insert key value newMap
    else
        match findCell key map.MaxSize map.Storage (calculateHash map.MaxSize key) 0 with
        | Some currentIndex ->
            let newStorage = Array.copy map.Storage
            newStorage.[currentIndex] <- Some(key, value)

            { map with
                Storage = newStorage
                Size = map.Size + 1 }
        | None -> map

let delete (key: 'Key) (map: OpenAddressHashMap<'Key, 'Value>) : OpenAddressHashMap<'Key, 'Value> =
    match findCell key map.MaxSize map.Storage (calculateHash map.MaxSize key) 0 with
    | Some currentIndex ->
        let newStorage = Array.copy map.Storage
        newStorage.[currentIndex] <- None

        { map with
            Storage = newStorage
            Size = map.Size - 1 }
    | None -> map

let collectValue (key: 'Key) (map: OpenAddressHashMap<'Key, 'Value>) : 'Value option =
    match findCell key map.MaxSize map.Storage (calculateHash map.MaxSize key) 0 with
    | Some currentIndex ->
        match map.Storage.[currentIndex] with
        | Some (_, v) -> Some v
        | None -> None
    | None -> None

let filterMap
    (condition: ('Key * 'Value) -> bool)
    (map: OpenAddressHashMap<'Key, 'Value>)
    : OpenAddressHashMap<'Key, 'Value> =
    let filteredItems =
        Array.fold
            (fun accumulator element ->
                match element with
                | Some (k, v) when condition (k, v) -> (k, v) :: accumulator
                | _ -> accumulator)
            []
            map.Storage

    // :: - значение в начало списка

    let newHashMap =
        { MaxSize = map.MaxSize
          Storage = Array.create map.MaxSize None
          Size = 0 }

    List.fold (fun accumulator (k, v) -> insert k v accumulator) newHashMap filteredItems

let map
    (mapper: ('Key * 'Value) -> ('Key * 'Value))
    (map: OpenAddressHashMap<'Key, 'Value>)
    : OpenAddressHashMap<'Key, 'Value> =
    let newStorage = Array.create map.MaxSize None

    let updatedStorage =
        Array.fold
            (fun (storage: ('Key * 'Value) option array) element ->
                match element with
                | Some (k, v) ->
                    let (newKey, newValue) = mapper (k, v)

                    match findCell newKey map.MaxSize storage (calculateHash map.MaxSize newKey) 0 with
                    | Some currentIndex ->
                        storage.[currentIndex] <- Some(newKey, newValue)
                        storage
                    | None -> storage
                | None -> storage)
            newStorage
            map.Storage

    { map with Storage = updatedStorage }

let foldLeft
    (aggregator: 'State -> ('Key * 'Value) -> 'State)
    (state: 'State)
    (map: OpenAddressHashMap<'Key, 'Value>)
    : 'State =
    Array.fold
        (fun accumulator element ->
            match element with
            | Some (k, v) -> aggregator accumulator (k, v)
            | None -> accumulator)
        state
        map.Storage

let foldRight
    (aggregator: ('Key * 'Value) -> 'State -> 'State)
    (state: 'State)
    (map: OpenAddressHashMap<'Key, 'Value>)
    : 'State =
    Array.foldBack
        (fun element accumulator ->
            match element with
            | Some (k, v) -> aggregator (k, v) accumulator
            | None -> accumulator)
        map.Storage
        state

let combine
    (firstHashMap: OpenAddressHashMap<'Key, 'Value>)
    (secondHashMap: OpenAddressHashMap<'Key, 'Value>)
    : OpenAddressHashMap<'Key, 'Value> =
    let newMaxSize = max firstHashMap.MaxSize secondHashMap.MaxSize
    let newStorage = Array.create newMaxSize None

    let insertAll (storage: ('Key * 'Value) option array) (map: OpenAddressHashMap<'Key, 'Value>) =
        Array.fold
            (fun updatedStorage element ->
                match element with
                | Some (k, v) ->
                    match findCell k newMaxSize updatedStorage (calculateHash newMaxSize k) 0 with
                    | Some currentIndex ->
                        updatedStorage.[currentIndex] <- Some(k, v)
                        updatedStorage
                    | None -> updatedStorage
                | None -> updatedStorage)
            storage
            map.Storage

    let combinedStorage = insertAll (insertAll newStorage firstHashMap) secondHashMap

    { MaxSize = newMaxSize
      Storage = combinedStorage
      Size = firstHashMap.Size + secondHashMap.Size }

let createEmptyHashMap (maxSize: int) : OpenAddressHashMap<'Key, 'Value> =
    { MaxSize = maxSize
      Storage = Array.create maxSize None
      Size = 0 }
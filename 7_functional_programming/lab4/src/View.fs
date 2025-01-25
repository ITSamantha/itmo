module Minesweeper.View

open Fable.React
open Fable.React.Props
open Types
open GameLogic

let title content =
    h1 [ ClassName "title" ] [ str content ]

let subtitle content =
    h2 [ ClassName "subtitle" ] [ str content ]

let showIcon label =
    span [ ClassName "icon" ] [
        i [ ClassName $"fa fa-{label}" ] []
    ]

let showGrid titleText presentBox model dispatch =
    let cellsTemplate = $"repeat({getSize model.map}, 1fr)"
    div [ ] [
        title titleText

        div [
            ClassName "minefield"
            Style [
                GridTemplateColumns cellsTemplate
                GridTemplateRows cellsTemplate
            ]
        ] (
            model.map
            |> Array.mapi presentBox
            |> Array.toList
        )

        button [
            classList [("reset-button", true); ("btn", true)]
            OnClick (fun _ -> dispatch ResetGame)
        ] [ str "Reset the game" ]
    ]

let showBox isDetonatedMine _ box =
    match box with
    | Mine ->
        let className = if isDetonatedMine then "minebox detonated" else "minebox"
        span [ ClassName className ] [ showIcon "bomb" ]
    | MineProximity nearbyMines ->
        span [
            ClassName $"minebox color-number-{nearbyMines}"
        ] [ str (string nearbyMines) ]
    | Empty ->
        span [ ClassName "minebox" ] []

let private showRawHotBox dispatch boxIndex content =
    button [
        ClassName "minebox hot-minebox"
        OnClick (fun _ -> dispatch (Reveal boxIndex))
        OnContextMenu (fun e ->
            e.preventDefault()
            dispatch (ToggleFlagMine boxIndex)
        )
    ] content

let showHotBox dispatch mbRevealedState boxIndex box =
    match mbRevealedState with
    | Some Open -> showBox false boxIndex box
    | Some FlaggedMine ->
        [ showIcon "question" ] |> showRawHotBox dispatch boxIndex
    | None -> showRawHotBox dispatch boxIndex []

let view model dispatch =
    let partialApp =
        match model.gameState with
        | Won ->
            showGrid
                "You won!🏆"
                (showBox false)
        | Lost detonatedMine ->
            showGrid
                "You triggered a mine!😢"
                (fun boxIndex box -> showBox (boxIndex = detonatedMine) boxIndex box)
        | Running ->
            showGrid
                "Let`s start!✅"
                (fun boxIndex box ->
                    showHotBox dispatch (model.revealed |> Map.tryFind boxIndex) boxIndex box
                )
    partialApp model dispatch

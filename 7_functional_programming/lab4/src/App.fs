module App

open Fable.React
open Fable.React.Props
open Elmish
open Elmish.React
open Minesweeper.Types
open Minesweeper.State
open Minesweeper.View
open Fable.Core.JsInterop

importAll "../sass/main.sass";


Program.mkProgram init update view
|> Program.withReactBatched "app"
|> Program.run

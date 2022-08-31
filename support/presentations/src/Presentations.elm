module Presentations exposing (main)

import Browser
import Html exposing (Html)
import Html.Attributes as Attribute
import Http
import Presentation exposing (Presentation)
import Json.Decode as Decode

main : Program () Model Msg
main =
    let
        model =
            Model
                { presentations = []
                , problem = Nothing
                }

        cmd =
            Http.get
                { url = "presentations.json"
                , expect = Http.expectJson Received <| Decode.list Presentation.decoder
                }
    in
    Browser.element
        { init = \_ -> ( model, cmd )
        , view = view
        , update = update
        , subscriptions = subscriptions
        }


type Model
    = Model
        { presentations : List Presentation
        , problem : Maybe Http.Error
        }


view : Model -> Html Msg
view (Model { presentations }) =
    let
        viewPresentation : Presentation -> Html msg
        viewPresentation presentation =
            Html.li []
                [ Html.a [ Attribute.href <| Presentation.url presentation ] [ Html.text <| Presentation.name presentation ]
                ]
    in
    Html.div []
        [ Html.h1 [] [ Html.text "Sessions" ]
        , Html.ul [] <| List.map viewPresentation presentations
        ]


type Msg
    = Received (Result Http.Error (List Presentation))


update : Msg -> Model -> ( Model, Cmd msg )
update msg (Model model) =
    case msg of
        Received (Err error) ->
            ( Model { model | problem = Just error }, Cmd.none )

        Received (Ok presentations) ->
            ( Model { model | presentations = presentations }, Cmd.none )


subscriptions : Model -> Sub Msg
subscriptions _ =
    Sub.none

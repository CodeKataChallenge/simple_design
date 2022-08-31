module Presentation exposing (Presentation, decoder, encode, name, url)

import Json.Decode as Decode exposing (Decoder)
import Json.Encode as Encode exposing (Value)


type Presentation
    = Presentation
        { name : String
        , url : String
        }


name : Presentation -> String
name (Presentation presentation) =
    presentation.name


url : Presentation -> String
url (Presentation presentation) =
    presentation.url


encode : Presentation -> Value
encode presentation =
    Encode.object
        [ ( "name", Encode.string <| name presentation )
        , ( "url", Encode.string <| url presentation )
        ]


decoder : Decoder Presentation
decoder =
    let
        construct : String -> String -> Presentation
        construct presentationName presentationUrl =
            Presentation
                { name = presentationName
                , url = presentationUrl
                }
    in
    Decode.map2 construct
        (Decode.field "name" Decode.string)
        (Decode.field "url" Decode.string)

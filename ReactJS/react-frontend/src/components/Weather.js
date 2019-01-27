import React from "react";


const Weather = (props) => {

  return(

          <div>
            {props.city && props.country && <p>Location: {props.city}, {props.country}</p>}
            {props.temperature && <p> Temperature: {props.temperature}</p>}
            {props.humidity && <p>Humiditiy: {props.humidity}</p>}
            {props.description && <p>Conditions: {props.description}</p>}
            {props.error && <p>Error: {props.error} </p>}
          </div>


        );


}

export default Weather;

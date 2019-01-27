const APIURL = 'localhost:8000'

const get_services = () =>{
    fetch(APIURL+'/services/')
}

const get_devices = () =>{
    fetch(APIURL+'/devices/')
}

const get_rates_by_device_and_time_frame = (deviceId, startTime, endTime) =>{
    fetch(APIURL+'/rates/?time__gte=' + startTime + '&time__lte=' + endTime + '&device=' + deviceId)
}
// const post_house_size = () =>{
//     fetch(APIURL+/house/)
// }
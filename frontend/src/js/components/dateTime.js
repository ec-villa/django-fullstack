import moment from 'moment';

const time = moment().subtract(4, 'days').format('MMMM Do YYYY, h:mm:ss a');
const spanTagEle = document.getElementById("datetime").innerHTML = time.toLocaleString();
console.log('moment: ', time);

console.log('hello: ');
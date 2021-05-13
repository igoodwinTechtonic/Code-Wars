function humanReadable(time) {
  let date = new Date(time * 1000).toJSON().split('T');
  let fTime = date[1].split(/\./)[0];
  if (time < 3600 * 24) return fTime;
  else {
    let timeParts = fTime.split(':');
    let hours = Math.floor(time / 3600);
    return `${hours}:${timeParts[1]}:${timeParts[2]}`
  }
}

function humanReadable(seconds) {
  const hours = Math.floor(seconds / (60 * 60));
  const minutes = Math.floor(seconds / 60) % 60;
  const newSeconds = seconds % 60;
  return `${formatNumber(hours)}:${formatNumber(minutes)}:${formatNumber(newSeconds)}`;
}
const formatNumber = (number) => {
  return number < 10 ? `0${number}` : number;
}

console.log(humanReadable(0) == '00:00:00');
console.log(humanReadable(5) == '00:00:05');
console.log(humanReadable(60) == '00:01:00');
console.log(humanReadable(86399) == '23:59:59');
console.log(humanReadable(359999) == '99:59:59');
console.log(humanReadable(42300) === '11:45:00');

/*
  if (time < 0 || time > 360000) return;
  let date = new Date(time * 1000).toJSON().split('T');
  let timeParts = date[1].split(/\.|:/);
  let hours = Number(timeParts[0]) + 24 * Math.floor(time / (3600 * 24));
  return `${Number(timeParts[0]) < 10 ? timeParts[0] : hours}:${timeParts[1]}:${timeParts[2]}`;
*/

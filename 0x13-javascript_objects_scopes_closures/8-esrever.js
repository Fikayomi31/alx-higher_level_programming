#!/usr/bin/node

exports.esrever = function (list) {
  const reverseArray = [];
  for (let i = list.length - 1; i >= 0; i--) {
    reverseArray.push(list[i]);
  }
  console.log(reverseArray);
};

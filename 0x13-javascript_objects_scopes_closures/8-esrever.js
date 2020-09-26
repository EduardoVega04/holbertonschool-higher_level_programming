#!/usr/bin/node
/*  function that returns the reversed version of a list */
exports.esrever = function (list) {
  let swap = null;
  const listLength = list.length;
  const j = listLength - 1;

  for (let i = 0; i < listLength; i++) {
    swap = list[i];
    list[i] = list[j];
    list[j] = swap;
  }

  return list;
};

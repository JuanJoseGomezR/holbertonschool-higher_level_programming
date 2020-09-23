#!/usr/bin/node
const request = require('request');

request.get(process.argv[2], (error, response, body) => {
  if (error) {
    throw error;
  }
  const derulo = JSON.parse(body);
  const userDict = {};

  for (const todo of derulo) {
    if (todo.completed === true) {
      if (userDict[todo.userId] === undefined) {
        userDict[todo.userId] = 1;
      } else {
        userDict[todo.userId] += 1;
      }
    }
  }
  console.log(userDict);
});

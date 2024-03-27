#!/usr/bin/node
// 6-completed_tasks.js
const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const todos = JSON.parse(body);
    const completed = {};
    todos.forEach((todo) => {
      if (todo.completed) {
        completed[todo.userId] = (completed[todo.userId] || 0) + 1;
      }
    });
    console.log(completed);
  }
});


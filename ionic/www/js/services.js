angular.module('starter.services', ['ngResource'])

.factory('Session', function ($resource) {
    return $resource('http://127.0.0.1:8000/hackathon/snippets/');
});
angular.module('starter.services', ['ngResource'])

.factory('Snippets', function ($resource) {
    return $resource('http://127.0.0.1:8000/hackathon/snippets/');
})

.factory('githubUser', function ($resource) {
    return $resource('http://127.0.0.1:8000/hackathon/githubUser/');
})

.factory('instagramUser', function ($resource){
	return $resource('http://localhost:8000/hackathon/instagramUser/');
})

.factory('steamSales', function ($resource){
	return $resource('http://127.0.0.1:8000/hackathon/steamDiscountedGames/');
})
'use strict';

restApp.controller('githubUserController', function($scope, githubUserFactory) {
    $scope.githubUser = {};
    
    $scope.githubUser = githubUserFactory.get().success(function(data) {
    	$scope.githubUser = data;
    	console.log(data);
    });
});

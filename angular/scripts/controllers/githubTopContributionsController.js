'use strict';

restApp.controller('githubTopContributionsController', function($scope, githubTopContributionsFactory) {
    $scope.githubTopContributions = {};
    
    $scope.githubTopContributions = githubTopContributionsFactory.get().success(function(data) {
    	$scope.githubTopContributions = data;
    	console.log(data);
    });
});

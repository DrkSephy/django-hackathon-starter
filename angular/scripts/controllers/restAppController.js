'use strict';

restApp.controller('restAppController', function($scope, restAppFactory) {
    $scope.restData = {};
    
    $scope.restData = restAppFactory.get().success(function(data) {
    	$scope.restData = data;
    	console.log(data);
    });
});

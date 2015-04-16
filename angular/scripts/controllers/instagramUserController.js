'use strict';

restApp.controller('instagramUserController', function($scope, instagramUserFactory){
	$scope.instagramUserData = {}

	$scope.instagramUserData = instagramUserFactory.get().success(function(data){
		$scope.instagramUserData = data;

		console.log(data);

	})

})
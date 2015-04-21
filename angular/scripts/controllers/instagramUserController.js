'use strict';

restApp.controller('instagramUserController', function($scope, instagramUserFactory, instagramUserMediaFactory){
	$scope.instagramUserData = {};
	$scope.instagramUserMediaData = {};

	$scope.instagramUserData = instagramUserFactory.get().success(function(data){
		$scope.instagramUserData = data;

		console.log(data);
	});
	
	$scope.instagramUserMediaData = instagramUserMediaFactory.get().success(function(data){
		$scope.instagramUserMediaData = data;

		console.log(data);
	});

})
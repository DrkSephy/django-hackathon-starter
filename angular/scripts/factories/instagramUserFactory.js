'use strict';

restApp.factory('instagramUserFactory', function($http){
	return {
		get: function(){
			return $http({
				url: 'http://localhost:8000/hackathon/instagramUser/',
				method: 'GET',
			});
		}
	};
});
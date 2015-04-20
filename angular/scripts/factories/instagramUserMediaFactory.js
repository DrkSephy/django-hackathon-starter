'use strict';

restApp.factory('instagramUserMediaFactory', function($http){
	return {
		get: function(){
			return $http({
				url: 'http://localhost:8000/hackathon/instagramUserMedia/',
				method: 'GET',
			});
		}
	};
});
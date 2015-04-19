angular.module('starter.controllers', ['starter.services'])

.controller('AppCtrl', function($scope, $ionicModal, $timeout) {

})

.controller('SnippetsCtrl', function($scope, Snippets) {
    $scope.snippets = Snippets.query();
})

.controller('githubUserCtrl', function($scope, githubUser) {
    $scope.githubUserData = githubUser.get();
})

.controller('instagramUserCtrl', function($scope, instagramUser, instagramUserMedia){
	$scope.instagramUserData = instagramUser.get();
	$scope.instagramUserMediaData = instagramUserMedia.get();
})

.controller('steamSalesCtrl', function($scope, steamSales){
	$scope.sales = steamSales.get();
});


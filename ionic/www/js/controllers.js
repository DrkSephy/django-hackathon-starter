angular.module('starter.controllers', ['starter.services'])

.controller('AppCtrl', function($scope, $ionicModal, $timeout) {

})

.controller('SnippetsCtrl', function($scope, Snippets) {
    $scope.snippets = Snippets.query();
})

.controller('githubUserCtrl', function($scope, githubUser) {
    $scope.githubUserData = githubUser.get();
})

.controller('instagramUserCtrl', function($scope, instagramUser){
	$scope.instagramUserData = instagramUser.get();
})


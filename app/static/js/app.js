// Your JavaScript Code here
var app = angular.module('AngApp', []);
app.controller('MainCtrl', function($scope, $http){
	$http.get("/api/thumbnails").then(function(response){
		$scope.thumbnails = response.data.thumbnails;
	});
})
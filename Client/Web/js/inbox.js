var securemail = angular.module('securemail', []);

securemail.controller('Register', function($scope, $http) {
  $scope.registerClick = function(){
    $http.get('http://86.45.70.108:8080/register').
        then(function(response) {
            $scope.register = response.data;
            window.alert("Details: "+$scope.register);
        });
  }
});

securemail.controller('RequestInbox', function($scope, $http) {
  $scope.requestInboxClick = function(){
    $http.get('http://86.45.70.108:8080/{'+$scope.id+'}:{'+$scope.secret+'}').
        then(function(response) {
            $scope.response = response.data;
            window.alert("Inbox: "+$scope.response);
        });
  }
});

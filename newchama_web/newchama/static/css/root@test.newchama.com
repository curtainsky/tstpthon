/*!
 * Bootstrap v3.2.0 (http://getbootstrap.com)
 * Copyright 2011-2014 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE)
 */

.btn-default,
.btn-primary,
.btn-success,
.btn-info,
.btn-warning,
.btn-danger {
  text-shadow: 0 -1px 0 rgba(0, 0, 0, .2);
  -webkit-box-shadow: inset 0 1px 0 rgba(255, 255, 255, .15), 0 1px 1px rgba(0, 0, 0, .075);
          box-shadow: inset 0 1px 0 rgba(255, 255, 255, .15), 0 1px 1px rgba(0, 0, 0, .075);
}
.btn-default:active,
.btn-primary:active,
.btn-success:active,
.btn-info:active,
.btn-warning:active,
.btn-danger:active,
.btn-default.active,
.btn-primary.active,
.btn-success.active,
.btn-info.active,
.btn-warning.active,
.btn-danger.active {
  -webkit-box-shadow: inset 0 3px 5px rgba(0, 0, 0, .125);
          box-shadow: inset 0 3px 5px rgba(0, 0, 0, .125);
}
.btn:active,
.btn.active {
  background-image: none;
}
.btn-default {
  text-shadow: 0 1px 0 #fff;
  background-image: -webkit-linear-gradient(top, #fff 0%, #e0e0e0 100%);
  background-image:      -o-linear-gradient(top, #fff 0%, #e0e0e0 100%);
  background-image: -webkit-gradient(linear, left top, left bottom, from(#fff), to(#e0e0e0));
  background-image:         linear-gradient(to bottom, #fff 0%, #e0e0e0 100%);
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ffffffff', endColorstr='#ffe0e0e0', GradientType=0);
  filter: progid:DXImageTransform.Microsoft.gradient(enabled = false);
  background-repeat: repeat-x;
  border-color: #dbdbdb;
  border-color: #ccc;
}
.btn-default:hover,
.btn-default:focus {
  background-color: #e0e0e0;
  background-position: 0 -15px;
}
.btn-default:active,
.btn-default.active {
  background-color: #e0e0e0;
  border-color: #dbdbdb;
}
.btn-default:disabled,
.btn-default[disabled] {
  background-color: #e0e0e0;
  background-image: none;
}
.btn-primary {
  background-image: -webkit-linear-gradient(top, #428bca 0%, #2d6ca2 100%);
  background-image:      -o-linear-gradient(top, #428bca 0%, #2d6ca2 100%);
  background-image: -webkit-gradient(linear, left top, left bottom, from(#428bca), to(#2d6ca2));
  background-image:         linear-gradient(to bottom, #428bca 0%, #2d6ca2 100%);
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff428bca', endColorstr='#ff2d6ca2', GradientType=0);
  filter: progid:DXImageTransform.Microsoft.gradient(enabled = false);
  background-repeat: repeat-x;
  border-color: #2b669a;
}
.btn-primary:hover,
.btn-primary:focus {
  background-color: #2d6ca2;
  background-position: 0 -15px;
}
.btn-primary:active,
.btn-primary.active {
  background-color: #2d6ca2;
  border-color: #2b669a;
}
.btn-primary:disabled,
.btn-primary[disabled] {
  background-color: #2d6ca2;
  background-image: none;
}
.btn-success {
  background-image: -webkit-linear-gradient(top, #5cb85c 0%, #419641 100%);
  background-image:      -o-linear-gradient(top, #5cb85c 0%, #419641 100%);
  background-image: -webkit-gradient(linear, left top, left bottom, from(#5cb85c), to(#419641));
  background-image:         linear-gradient(to bottom, #5cb85c 0%, #419641 100%);
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff5cb85c', endColorstr='#ff419641', GradientType=0);
  filter: progid:DXImageTransform.Microsoft.gradient(enabled = false);
  background-repeat: repeat-x;
  border-color: #3e8f3e;
}
.btn-success:hover,
.btn-success:focus {
  background-color: #419641;
  background-position: 0 -15px;
}
.btn-success:active,
.btn-success.active {
  background-color: #419641;
  border-color: #3e8f3e;
}
.btn-success:disabled,
.btn-success[disabled] {
  background-color: #419641;
  background-image: none;
}
.btn-info {
  background-image: -webkit-linear-gradient(top, #5bc0de 0%, #2aabd2 100%);
  background-image:      -o-linear-gradient(top, #5bc0de 0%, #2aabd2 100%);
  background-image: -webkit-gradient(linear, left top, left bottom, from(#5bc0de), to(#2aabd2));
  background-image:         linear-gradient(to bottom, #5bc0de 0%, #2aabd2 100%);
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff5bc0de', endColorstr='#ff2aabd2', GradientType=0);
  filter: progid:DXImageTransform.Microsoft.gradient(enabled = false);
  background-repeat: repeat-x;
  border-color: #28a4c9;
}
.btn-info:hover,
.btn-info:focus {
  background-color: #2aabd2;
  background-position: 0 -15px;
}
.btn-info:active,
.btn-info.active {
  background-color: #2aabd2;
  border-color: #28a4c9;
}
.btn-info:disabled,
.btn-info[disabled] {
  background-color: #2aabd2;
  background-image: none;
}
.btn-warning {
  background-image: -webkit-linear-gradient(top, #f0ad4e 0%, #eb9316 100%);
  background-image:      -o-linear-gradient(top, #f0ad4e 0%, #eb9316 100%);
  background-image: -webkit-gradient(linear, left top, left bottom, from(#f0ad4e), to(#eb9316));
  background-image:         linear-gradient(to bottom, #f0ad4e 0%, #eb9316 100%);
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#fff0ad4e', endColorstr='#ffeb9316', GradientType=0);
  filter: progid:DXImageTransform.Microsoft.gradient(enabled = false);
  background-repeat: repeat-x;
  border-color: #e38d13;
}
.btn-warning:hover,
.btn-warning:focus {
  background-color: #eb9316;
  background-position: 0 -15px;
}
.btn-warning:active,
.btn-warning.active {
  background-color: #eb9316;
  border-color: #e38d13;
}
.btn-warning:disabled,
.btn-warning[disabled] {
  background-color: #eb9316;
  background-image: none;
}
.btn-danger {
  background-image: -webkit-linear-gradient(top, #d9534f 0%, #c12e2a 100%);
  background-image:      -o-linear-gradient(top, #d9534f 0%, #c12e2a 100%);
  background-image: -webkit-gradient(linear, left top, left bottom, from(#d9534f), to(#c12e2a));
  background-image:         linear-gradient(to bottom, #d9534f 0%, #c12e2a 100%);
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ffd9534f', endColorstr='#ffc12e2a', GradientType=0);
  filter: progid:DXImageTransform.Microsoft.gradient(enabled = false);
  background-repeat: repeat-x;
  border-color: #b92c28;
}
.btn-danger:hover,
.btn-danger:focus {
  background-color: #c12e2a;
  background-position: 0 -15px;
}
.btn-danger:active,
.btn-danger.active {
  background-color: #c12e2a;
  border-color: #b92c28;
}
.btn-danger:disabled,
.btn-danger[disabled] {
  background-color: #c12e2a;
  background-image: none;
}
.thumbnail,
.img-thumbnail {
  -webkit-box-shadow: 0 1px 2px rgba(0, 0, 0, .075);
          box-shadow: 0 1px 2px rgba(0, 0, 0, .075);
}
.dropdown-menu > li > a:hover,
.dropdown-menu > li > a:focus {
  background-color: #e8e8e8;
  background-image: -webkit-linear-gradient(top, #f5f5f5 0%, #e8e8e8 100%);
  background-image:      -o-linear-gradient(top, #f5f5f5 0%, #e8e8e8 100%);
  background-image: -webkit-gradient(linear, left top, left bottom, from(#f5f5f5), to(#e8e8e8));
  background-image:         linear-gradient(to bottom, #f5f5f5 0%, #e8e8e8 100%);
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#fff5f5f5', endColorstr='#ffe8e8e8', GradientType=0);
  background-repeat: repeat-x;
}
.dropdown-menu > .active > a,
.dropdown-menu > .active > a:hover,
.dropdown-menu > .active > a:focus {
  background-color: #357ebd;
  background-image: -webkit-linear-gradient(top, #428bca 0%, #357ebd 100%);
  background-image:      -o-linear-gradient(top, #428bca 0%, #357ebd 100%);
  background-image: -webkit-gradient(linear, left top, left bottom, from(#428bca), to(#357ebd));
  background-image:         linear-gradient(to bottom, #428bca 0%, #357ebd 100%);
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff428bca', endColorstr='#ff357ebd', GradientType=0);
  background-repeat: repeat-x;
}
.navbar-default {

  background-color:#2c2c2c;
  color: #777;
   
  background-image: -webkit-linear-gradient(top, #2c2c2c 0%, #050505 100%);
  background-image:      -o-linear-gradient(top, #2c2c2c 0%, #050505 100%);
  background-image: -webkit-gradient(linear, left top, left bottom, from(#2c2c2c), to(#050505));
  background-image:         linear-gradient(to bottom, #2c2c2c 0%, #050505 100%);
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff2c2c2c', endColorstr='#ff050505', GradientType=0);
  filter: progid:DXImageTransform.Microsoft.gradient(enabled = false);
  background-repeat: repeat-x;
  
  border:none;
  border-radius: 0px;
  -webkit-box-shadow: inset 0 1px 0 rgba(255, 255, 255, .15), 0 1px 5px rgba(0, 0, 0, .075);
          box-shadow: inset 0 1px 0 rgba(255, 255, 255, .15), 0 1px 5px rgba(0, 0, 0, .075);
}
.navbar-default .navbar-nav > .active > a {
  background-color:#ebebeb;
  background-image: -webkit-linear-gradient(top, #ebebeb 0%, #f3f3f3 100%);
  background-image:      -o-linear-gradient(top, #ebebeb 0%, #f3f3f3 100%);
  background-image: -webkit-gradient(linear, left top, left bottom, from(#ebebeb), to(#f3f3f3));
  background-image:         linear-gradient(to bottom, #ebebeb 0%, #f3f3f3 100%);
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ffebebeb', endColorstr='#fff3f3f3', GradientType=0);
  background-repeat: repeat-x;
  -webkit-box-shadow: inset 0 5px 20px rgba(0, 0, 0, .3);
          box-shadow: inset 0 5px 20px rgba(0, 0, 0, .3);
}
.navbar-brand,

.navbar-nav > li > a {
  text-shadow: 0 0px 0 rgba(255, 255, 255, .25);
}
.navbar-inverse {
  background-image: -webkit-linear-gradient(top, #3c3c3c 0%, #222 50%);
  background-image:      -o-linear-gradient(top, #3c3c3c 0%, #222 50%);
  background-image: -webkit-gradient(linear, left top, left center, from(#3c3c3c), to(#222));
  background-image:         linear-gradient(to bottom, #3c3c3c 0%, #222 50%);
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff3c3c3c', endColorstr='#ff222222', GradientType=0);
  filter: progid:DXImageTransform.Microsoft.gradient(enabled = false);
  background-repeat: repeat-x;
}
.navbar-inverse .navbar-nav > .active > a {
  background-image: -webkit-linear-gradient(top, #222 0%, #282828 100%);
  background-image:      -o-linear-gradient(top, #222 0%, #282828 100%);
  background-image: -webkit-gradient(linear, left top, left bottom, from(#222), to(#282828));
  background-image:         linear-gradient(to bottom, #222 0%, #282828 100%);
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff222222', endColorstr='#ff282828', GradientType=0);
  background-repeat: repeat-x;
  -webkit-box-shadow: inset 0 3px 9px rgba(0, 0, 0, .25);
          box-shadow: inset 0 3px 9px rgba(0, 0, 0, .25);
}
.navbar-inverse .navbar-brand,
.navbar-inverse .navbar-nav > li > a {
  text-shadow: 0 -1px 0 rgba(0, 0, 0, .25);
}
.navbar-static-top,
.navbar-fixed-top,
.navbar-fixed-bottom {
  border-radius: 0;
}
.alert {
  border-radius: 0px;
  padding: 6px 15px;
  text-shadow: 0 1px 0 rgba(255, 255, 255, .2);
  -webkit-box-shadow: inset 0 1px 0 rgba(255, 255, 255, .25), 0 1px 2px rgba(0, 0, 0, .05);
          box-shadow: inset 0 1px 0 rgba(255, 255, 255, .25), 0 1px 2px rgba(0, 0, 0, .05);
}

.alert .close{font-size: 14px;}
.alert-success {
 
  border-color: #b2dba1;
}
.alert-info {
  
  border-color: #9acfea;
}
.alert-warning {
  
  border-color: #f5e79e;
}
.alert-danger {
 
  border-color: #dca7a7;
}
.progress {
  background-image: -webkit-linear-gradient(top, #ebebeb 0%, #f5f5f5 100%);
  background-image:      -o-linear-gradient(top, #ebebeb 0%, #f5f5f5 100%);
  background-image: -webkit-gradient(linear, left top, left bottom, from(#ebebeb), to(#f5f5f5));
  background-image:         linear-gradient(to bottom, #ebebeb 0%, #f5f5f5 100%);
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ffebebeb', endColorstr='#fff5f5f5', GradientType=0);
  background-repeat: repeat-x;
}
.progress-bar {
  border-radius: 0px;
  background-image: -webkit-linear-gradient(top, #428bca 0%, #3071a9 100%);
  background-image:      -o-linear-gradient(top, #428bca 0%, #3071a9 100%);
  background-image: -webkit-gradient(linear, left top, left bottom, from(#428bca), to(#3071a9));
  background-image:         linear-gradient(to bottom, #428bca 0%, #3071a9 100%);
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff428bca', endColorstr='#ff3071a9', GradientType=0);
  background-repeat: repeat-x;
}
.progress-bar-success {
  background-image: -webkit-linear-gradient(top, #5cb85c 0%, #449d44 100%);
  background-image:      -o-linear-gradient(top, #5cb85c 0%, #449d44 100%);
  background-image: -webkit-gradient(linear, left top, left bottom, from(#5cb85c), to(#449d44));
  background-image:         linear-gradient(to bottom, #5cb85c 0%, #449d44 100%);
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff5cb85c', endColorstr='#ff449d44', GradientType=0);
  background-repeat: repeat-x;
}
.progress-bar-info {
  background-image: -webkit-linear-gradient(top, #5bc0de 0%, #31b0d5 100%);
  background-image:      -o-linear-gradient(top, #5bc0de 0%, #31b0d5 100%);
  background-image: -webkit-gradient(linear, left top, left bottom, from(#5bc0de), to(#31b0d5));
  background-image:         linear-gradient(to bottom, #5bc0de 0%, #31b0d5 100%);
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff5bc0de', endColorstr='#ff31b0d5', GradientType=0);
  background-repeat: repeat-x;
}
.progress-bar-warning {
  background-image: -webkit-linear-gradient(top, #f0ad4e 0%, #ec971f 100%);
  background-image:      -o-linear-gradient(top, #f0ad4e 0%, #ec971f 100%);
  background-image: -webkit-gradient(linear, left top, left bottom, from(#f0ad4e), to(#ec971f));
  background-image:         linear-gradient(to bottom, #f0ad4e 0%, #ec971f 100%);
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#fff0ad4e', endColorstr='#ffec971f', GradientType=0);
  background-repeat: repeat-x;
}
.progress-bar-danger {
  background-image: -webkit-linear-gradient(top, #d9534f 0%, #c9302c 100%);
  background-image:      -o-linear-gradient(top, #d9534f 0%, #c9302c 100%);
  background-image: -webkit-gradient(linear, left top, left bottom, from(#d9534f), to(#c9302c));
  background-image:         linear-gradient(to bottom, #d9534f 0%, #c9302c 100%);
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ffd9534f', endColorstr='#ffc9302c', GradientType=0);
  background-repeat: repeat-x;
}
.progress-bar-striped {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, .15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, .15) 50%, rgba(255, 255, 255, .15) 75%, transparent 75%, transparent);
  background-image:      -o-linear-gradient(45deg, rgba(255, 255, 255, .15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, .15) 50%, rgba(255, 255, 255, .15) 75%, transparent 75%, transparent);
  background-image:         linear-gradient(45deg, rgba(255, 255, 255, .15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, .15) 50%, rgba(255, 255, 255, .15) 75%, transparent 75%, transparent);
}
.list-group {
  border-radius: 4px;
  -webkit-box-shadow: 0 1px 2px rgba(0, 0, 0, .075);
          box-shadow: 0 1px 2px rgba(0, 0, 0, .075);
}
.list-group-item.active,
.list-group-item.active:hover,
.list-group-item.active:focus {
  text-shadow: 0 -1px 0 #3071a9;
  background-image: -webkit-linear-gradient(top, #428bca 0%, #3278b3 100%);
  background-image:      -o-linear-gradient(top, #428bca 0%, #3278b3 100%);
  background-image: -webkit-gradient(linear, left top, left bottom, from(#428bca), to(#3278b3));
  background-image:         linear-gradient(to bottom, #428bca 0%, #3278b3 100%);
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff428bca', endColorstr='#ff3278b3', GradientType=0);
  background-repeat: repeat-x;
  border-color: #3278b3;
}
.panel {
  -webkit-box-shadow: 0 1px 2px rgba(0, 0, 0, .05);
          box-shadow: 0 1px 2px rgba(0, 0, 0, .05);
}

  /*
.panel-default > .panel-heading {
  
  background-image: -webkit-linear-gradient(top, #f5f5f5 0%, #e8e8e8 100%);
  background-image:      -o-linear-gradient(top, #f5f5f5 0%, #e8e8e8 100%);
  background-image: -webkit-gradient(linear, left top, left bottom, from(#f5f5f5), to(#e8e8e8));
  background-image:         linear-gradient(to bottom, #f5f5f5 0%, #e8e8e8 100%);
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#fff5f5f5', endColorstr='#ffe8e8e8', GradientType=0);
  background-repeat: repeat-x;

}
.panel-primary > .panel-heading {
  
  background-image: -webkit-linear-gradient(top, #428bca 0%, #357ebd 100%);
  background-image:      -o-linear-gradient(top, #428bca 0%, #357ebd 100%);
  background-image: -webkit-gradient(linear, left top, left bottom, from(#428bca), to(#357ebd));
  background-image:         linear-gradient(to bottom, #428bca 0%, #357ebd 100%);
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff428bca', endColorstr='#ff357ebd', GradientType=0);
  background-repeat: repeat-x;
  
}
.panel-success > .panel-heading {
  background-image: -webkit-linear-gradient(top, #dff0d8 0%, #d0e9c6 100%);
  background-image:      -o-linear-gradient(top, #dff0d8 0%, #d0e9c6 100%);
  background-image: -webkit-gradient(linear, left top, left bottom, from(#dff0d8), to(#d0e9c6));
  background-image:         linear-gradient(to bottom, #dff0d8 0%, #d0e9c6 100%);
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ffdff0d8', endColorstr='#ffd0e9c6', GradientType=0);
  background-repeat: repeat-x;
}
.panel-info > .panel-heading {
  background-image: -webkit-linear-gradient(top, #d9edf7 0%, #c4e3f3 100%);
  background-image:      -o-linear-gradient(top, #d9edf7 0%, #c4e3f3 100%);
  background-image: -webkit-gradient(linear, left top, left bottom, from(#d9edf7), to(#c4e3f3));
  background-image:         linear-gradient(to bottom, #d9edf7 0%, #c4e3f3 100%);
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ffd9edf7', endColorstr='#ffc4e3f3', GradientType=0);
  background-repeat: repeat-x;
}
.panel-warning > .panel-heading {
  background-image: -webkit-linear-gradient(top, #fcf8e3 0%, #faf2cc 100%);
  background-image:      -o-linear-gradient(top, #fcf8e3 0%, #faf2cc 100%);
  background-image: -webkit-gradient(linear, left top, left bottom, from(#fcf8e3), to(#faf2cc));
  background-image:         linear-gradient(to bottom, #fcf8e3 0%, #faf2cc 100%);
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#fffcf8e3', endColorstr='#fffaf2cc', GradientType=0);
  background-repeat: repeat-x;
}
.panel-danger > .panel-heading {
  background-image: -webkit-linear-gradient(top, #f2dede 0%, #ebcccc 100%);
  background-image:      -o-linear-gradient(top, #f2dede 0%, #ebcccc 100%);
  background-image: -webkit-gradient(linear, left top, left bottom, from(#f2dede), to(#ebcccc));
  background-image:         linear-gradient(to bottom, #f2dede 0%, #ebcccc 100%);
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#fff2dede', endColorstr='#ffebcccc', GradientType=0);
  background-repeat: repeat-x;
}

*/
.well {
  background-image: -webkit-linear-gradient(top, #e8e8e8 0%, #f5f5f5 100%);
  background-image:      -o-linear-gradient(top, #e8e8e8 0%, #f5f5f5 100%);
  background-image: -webkit-gradient(linear, left top, left bottom, from(#e8e8e8), to(#f5f5f5));
  background-image:         linear-gradient(to bottom, #e8e8e8 0%, #f5f5f5 100%);
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ffe8e8e8', endColorstr='#fff5f5f5', GradientType=0);
  background-repeat: repeat-x;
  border-color: #dcdcdc;
  -webkit-box-shadow: inset 0 1px 3px rgba(0, 0, 0, .05), 0 1px 0 rgba(255, 255, 255, .1);
          box-shadow: inset 0 1px 3px rgba(0, 0, 0, .05), 0 1px 0 rgba(255, 255, 255, .1);
}

/* ==Tables */
/* ----------------------------------------------- */
.table-bordered thead tr,
.table-bordered tfoot tr {
  background-color: #f3f3f3;
}
.table-bordered thead tr th,
.table-bordered tfoot tr th {
  color: #444;
  font-size: 12px;
  font-weight: 800;
  background-color: transparent;
  border-bottom-width: 1px;
  vertical-align: middle;
}
.table-bordered.table-highlight {
  border-top-color: #111;
}
.table-bordered.table-highlight thead tr:first-child {
  background-color: #363636;
}
.table-bordered.table-highlight thead tr:first-child th {
  color: #fff;
  font-weight: 600;
  border: 1px solid #2c2c2c;
}

/* ==Labels */
/* ----------------------------------------------- */
.label-primary {
  background-color: #e74c3c;
}
.label-primary[href]:hover,
.label-primary[href]:focus {
  background-color: #d62c1a;
}
.label-secondary {
  background-color: #428bca;
}
.label-secondary[href]:hover,
.label-secondary[href]:focus {
  background-color: #3071a9;
}
.label-tertiary {
  background-color: #bbbbbb;
}
.label-tertiary[href]:hover,
.label-tertiary[href]:focus {
  background-color: #a2a2a2;
}
.label-info {
  background-color: #5bc0de;
}
.label-info[href]:hover,
.label-info[href]:focus {
  background-color: #31b0d5;
}
.label-warning {
  background-color: #f0ad4e;
}
.label-warning[href]:hover,
.label-warning[href]:focus {
  background-color: #ec971f;
}

/* ==Modal */
/* ----------------------------------------------- */


.modal-content{border-radius: 0px;}

.modal-header{ padding: 10px 15px;}
.modal-footer{ padding: 10px 15px;}
.modal-body{font-size: 12px;}
.modal-title{font-size: 16px;}

.modal-backdrop {
  background-color: #ffffff;
}
.modal-backdrop.in {
  filter: alpha(opacity=60);
  -webkit-opacity: 0.6;
  -moz-opacity: 0.6;
  opacity: 0.6;
}
.modal-styled .modal-header {
 
  color: #fff;
  background-color: #333;
}
.modal-styled .modal-header .close {
  color: #fff;
  opacity: 1;
  text-shadow: none;
}
.modal-styled .modal-header .close:hover {
  filter: alpha(opacity=70);
  -webkit-opacity: 0.7;
  -moz-opacity: 0.7;
  opacity: 0.7;
}
.modal-styled .modal-footer {
  
  background-color: #eee;
  border-top: 1px solid #ddd;
}

/* ==Morris [.morris]*/
/* ----------------------------------------------- */
.morris-hover {
  position: absolute;
  z-index: 1000;
}
.morris-hover.morris-default-style {
  padding: 6px;
  color: #666;
  font-size: 12px;
  font-weight: 600;
  text-align: center;
  background: rgba(255, 255, 255, 0.8);
  border: solid 2px rgba(230, 230, 230, 0.8);
  -webkit-border-radius: 10px;
  -webkit-background-clip: padding-box;
  -moz-border-radius: 10px;
  -moz-background-clip: padding;
  border-radius: 10px;
  background-clip: padding-box;
}
.morris-hover.morris-default-style .morris-hover-row-label {
  margin: .25em 0;
  font-weight: 600;
}
.morris-hover.morris-default-style .morris-hover-point {
  margin: 0.1em 0;
  white-space: nowrap;
}



body{background: #343434; line-height: 1.2em; font-family:'Heiti SC',"Microsoft YaHei","Tahoma","SimSun","WenQuanYi Micro Hei"!important;}
.footer{background: #232524;  margin-bottom: 0px; color: #ccc; font-size: 12px; text-align: center; padding: 20px;}
.footer a{color: #ccc;}
.col-xs-1, .col-sm-1, .col-md-1, .col-lg-1, .col-xs-2, .col-sm-2, .col-md-2, .col-lg-2, .col-xs-3, .col-sm-3, .col-md-3, .col-lg-3, .col-xs-4, .col-sm-4, .col-md-4, .col-lg-4, .col-xs-5, .col-sm-5, .col-md-5, .col-lg-5, .col-xs-6, .col-sm-6, .col-md-6, .col-lg-6, .col-xs-7, .col-sm-7, .col-md-7, .col-lg-7, .col-xs-8, .col-sm-8, .col-md-8, .col-lg-8, .col-xs-9, .col-sm-9, .col-md-9, .col-lg-9, .col-xs-10, .col-sm-10, .col-md-10, .col-lg-10, .col-xs-11, .col-sm-11, .col-md-11, .col-lg-11, .col-xs-12, .col-sm-12, .col-md-12, .col-lg-12{
  padding-left: 5px; padding-right: 5px;
}
.table>thead>tr>th, .table>tbody>tr>th, .table>tfoot>tr>th, .table>thead>tr>td, .table>tbody>tr>td, .table>tfoot>tr>td{
  padding: 6px 15px; font-size: 12px;
}
button{border:none;}
.table-condensed>thead>tr>th, .table-condensed>tbody>tr>th, .table-condensed>tfoot>tr>th, .table-condensed>thead>tr>td, .table-condensed>tbody>tr>td, .table-condensed>tfoot>tr>td{
  padding: 3px 15px;
}
.pagination>li>a, .pagination>li>span{padding: 4px 10px; font-size: 12px;}
.dropdown-menu{font-size: 12px;}
@media (min-width: 768px) {
.form-control{padding: 2px 6px;border-radius:0px; height: 26px; font-size: 12px;}
}
caption{text-align: left; font-weight: bold; padding:6px 15px; background: #f1f1f1;}
.pagination{margin: 0px;}

.dropdown-menu{border-radius:0px;}

.form-horizontal .form-group{margin-left: 15px; margin-right: 15px;}

.form-horizontal .radio, .form-horizontal .checkbox, .form-horizontal .radio-inline, .form-horizontal .checkbox-inline{
  padding-top: 0px;
}

.nav-pills>li>a{
  font-size: 12px;
  color: #428bca;
}
.nav-pills>li.active>a, .nav-pills>li.active>a:hover, .nav-pills>li.active>a:focus{
  background-color: #428bca;
}


.navbar{border-radius:0px;}
.navbar-collapse{padding-left: 0px; padding-right: 0px; font-size: 13px;}

.navbar-brand{width: 350px; height: 20px; background: url(../images/logo.png) no-repeat; margin-left: 15px; margin-top: 20px; padding-left: 160px; font-size: 12px; color: #fff; }
.navbar-default .navbar-brand{padding-top: 5px;}


#newchama_nav{ background: #009dad; margin-top: 60px;}
#newchama_nav .navbar-nav>.active>a, #newchama_nav .navbar-nav>.active>a:hover, #newchama_nav .navbar-nav>.active>a:focus{
  color: #fff; background: #009dad;
  border-left: 1px solid #009dad;

}


@media (min-width: 768px) {

  .navbar-nav.navbar-right:last-child{margin-right: 0px;}
.navbar-search-form{ width: 300px;  height: 26px;margin-top: 15px; font-size: 12px; }
.navbar-search-form .input-group{ width: 300px; height: 26px;}
.navbar-search-form .input-group-btn{height: 26px;}
.navbar-search-form .form-control{height: 26px; border-right: none; background: #fff;border-radius:4px; }

.navbar-search-form .input-group-btn .btn{padding: 2px 6px; background: #fff; color: #0185c5; border-left: none;}


.input-group-btn{height: 26px;}
.form-control{height: 26px;border-radius:0px; }

.input-group-btn .btn{padding: 2px 6px;font-size: 12px; height: 26px; }
.input-group-addon{padding: 2px 6px; font-size: 12px; height: 26px; }

}


#newchama_nav .navbar-nav>li>a{color: #fff; border-right: 1px solid #016771; border-left: 1px solid #02b1c3;}


@media (min-width: 768px) {
#newchama_nav .navbar-nav>li>a{ width:98px;text-align: center; }
}

#newchama_nav .navbar-nav>li>a:hover, #newchama_nav .navbar-nav>li>a:focus{
   border-left: 1px solid #009dad;
  background: #009dad;
  -webkit-box-shadow: inset 0 5px 20px rgba(0, 0, 0, .3);
          box-shadow: inset 0 5px 20px rgba(0, 0, 0, .3);
}
#newchama_nav .navbar-nav > .active > a {
  
  -webkit-box-shadow: inset 0 5px 20px rgba(0, 0, 0, .3);
          box-shadow: inset 0 5px 20px rgba(0, 0, 0, .3);
}
#newchama_nav .navbar-nav>.open>a, #newchama_nav .navbar-nav>.open>a:hover, #newchama_nav .navbar-nav>.open>a:focus{
  background: #009dad;
  -webkit-box-shadow: inset 0 5px 20px rgba(0, 0, 0, .3);
          box-shadow: inset 0 5px 20px rgba(0, 0, 0, .3);
}

#newchama_nav .dropdown-menu{font-size: 13px;}


#newchama_main{background: #eee; margin-left: 15px; margin-right: 15px; margin-bottom: 20px; padding-top: 20px; min-height: 600px; max-width: 1280px; margin: 0 auto;}
.panel{border-radius:0px;}
.panel-title{font-size: 13px;  }
.panel-title a{color: #ccc;}
.panel-default > .panel-heading{ background: #444444 !important; color: #fff;border-color:#343434;border-top-left-radius:0px;border-top-right-radius:0px; border: none; padding: 8px 15px; }
.panel-body{font-size: 12px; padding: 8px 15px;}

.nav-tabs>li>a{border-radius:0;padding: 4px 6px;}
.nav-pills>li>a{border-radius:0;padding: 4px 6px;}


@media (max-width: 767px) {
#newchama_nav  .navbar-nav .open .dropdown-menu>li>a{
  color: #eee;
}
#newchama_nav  .navbar-nav .open .dropdown-menu>li>a:hover, #newchama_nav  .navbar-nav .open .dropdown-menu>li>a:focus{
  color: #fff;
}
}

@media (min-width: 768px) {

  #avatar-dropdown{ height: 60px; line-height: 60px; color: #f8f8f8; font-size: 13px;}
  #avatar-dropdown>li>a{ color: #f8f8f8;}
  #avatar-dropdown.open>a, #avatar-dropdown.open>a:hover, #avatar-dropdown.open>a:focus{
    background: none;
  }

  #avatar-dropdown .thumbnail{padding: 2px; margin-bottom: 0px;}
  #avatar-dropdown .dropdown-menu{
     font-size: 13px;
  }

  .navbar-right >li>a {height: 60px; line-height: 30px; padding: 15px 10px; font-size: 13px;}

  #avatar-dropdown .dropdown-menu:before {
    content: '';
    position: relative;
    z-index: 10601;
    display: inline-block;
    border-left: 7px solid transparent;
    border-right: 7px solid transparent;
    border-bottom: 7px solid #fff;
    position: absolute;
    top: -7px;
    left: 8px;
  }
  .navbar-right #avatar-dropdown .dropdown-menu:before {
    left: auto;
    right: 12px;
  }

  
}


/* ==Noticebar [.noticebar]*/
/* ----------------------------------------------- */


.navbar .noticebar > li > a .badge {
  padding-top: 4px;
  padding-bottom: 4px;
  font-size: 10px;
  background: transparent;
  border: 2px solid #e74c3c;
}
.navbar .noticebar > .open > a .badge {
  background: #e74c3c;
}
@media (min-width: 768px) {
  .navbar .noticebar{ height: 60px; line-height: 30px;  font-size: 13px;padding: 0px;}

  .navbar .noticebar .open>a, .navbar .noticebar .open>a:hover, .navbar .noticebar .open>a:focus{
      background: none;
    }

  .navbar .noticebar > li > a {
    max-height: 60px;
    color: #3c3c3c;
    font-size: 19px;
  }
  .navbar .noticebar > li > a:hover {
    color: #555555;
  }
  .navbar .noticebar > li > a .badge {
    position: absolute;
    top: 6px;
    right: 3px;
    border-top-right-radius: 100px;
    border-top-left-radius: 100px;
    border-bottom-right-radius: 100px;
    border-bottom-left-radius: 100px;
  }
  .navbar .noticebar > .open > a:after {
    content: '';
    position: relative;
    z-index: 1001;
    display: inline-block;
    border-left: 8px solid transparent;
    border-right: 8px solid transparent;
    border-bottom: 8px solid #fff;
    position: absolute;
    bottom: -2px;
    left: 50%;
    margin-left: -8px;
  }
}
.noticebar-empty {
  padding: 25px 35px !important;
  text-align: center;
}
.noticebar-empty-title {
  color: #e74c3c;
}
.noticebar-empty-text {
  color: #777;
}
.noticebar-menu-view-all {
  text-align: center;
}
.noticebar-menu {
  width: 325px;
}
.noticebar-menu .nav-header {
  padding: 6px 12px;
  font-size: 13px;
  font-weight: 600;
}
.noticebar-menu .nav-header a {
  font-weight: 400;
}
.noticebar-menu > li {
  display: table;
  width: 100%;
  padding: 0;
  margin-right: 0;
  margin-left: 0;
  border-bottom: 1px dotted #ccc;
}
.noticebar-menu > li:last-child {
  border-bottom: none;
}
.noticebar-menu > li > a {
  padding: 8px 12px;
  font-size: 12px;
  white-space: normal;
}
.noticebar-menu > li > a:hover {
  color: #444;
  background: #eee;
}
.noticebar-menu:before,
.noticebar-menu:after {
  display: none !important;
}
.navbar-visible-collapsed {
  display: inline;
}
@media (max-width: 768px) {
  .noticebar-menu {
    display: none !important;
  }
}
@media (min-width: 768px) {
  .navbar-visible-collapsed {
    display: none;
  }
}
.noticebar-item-image,
.noticebar-item-body {
  display: table-cell;
  vertical-align: middle;
}
.noticebar-item-image {
  width: 36px;
  font-size: 30px;
  text-align: center;
}
.noticebar-item-body {
  padding-left: 20px;
}
.noticebar-item-title {
  display: block;
}
.noticebar-item-time {
  display: block;
  color: #777;
}


/* ==news_list [.news_list1]*/
/* ----------------------------------------------- */

.news-list{
  width: 100%;
  padding: 0px;
  margin-bottom: 0px;

}
.news-list-empty {
  padding: 25px 35px !important;
  text-align: center;
}
.news-list-empty-title {
  color: #e74c3c;
}
.news-list-empty-text {
  color: #777;
}
.news-list-view-all {
  text-align: center;
  margin-bottom: 0px;
}
.news-list-view-all a{
  clear:both;
  padding: 8px 0px;
  font-size: 12px;
  white-space: normal;
  display: block;
  color: #333;
  text-decoration: none;
}

.news-list-view-all a:hover{
  color: #444;
  background: #eee;
}


.news-list-view-all2 {
  border-top: 1px dotted #ccc;
  text-align: center;
  margin-bottom: 0px;
}
.news-list-view-all2 a{
  clear:both;
  padding: 8px 0px;
  font-size: 12px;
  white-space: normal;
  display: block;
  color: #333;
  text-decoration: none;
}

.news-list-view-all2 a:hover{
  color: #444;
  background: #eee;
}

.news-list .nav-header {
  padding: 6px 0px;
  font-size: 13px;
  font-weight: 600;
}
.news-list .nav-header a {
  font-weight: 400;
}
.news-list > li {
  display: table;
  width: 100%;
  padding: 0;
  margin-right: 0;
  margin-left: 0;
  border-bottom: 1px dotted #ccc;
}
.news-list li {list-style: none;}

.news-list > li:last-child {
  border-bottom: none;
}
.news-list > li.news-list-item {
  padding: 8px 0px;
  font-size: 12px;
  white-space: normal;
  display: block;
  color: #333;
  text-decoration: none;
}
.news-list > li > a.news-list-item {
  padding: 8px 0px;
  font-size: 12px;
  white-space: normal;
  display: block;
  color: #333;
  text-decoration: none;
}
.news-list > li > a.news-list-item:hover {
  color: #444;
  background: #eee;
}
.news-list:before,
.news-list:after {
  display: none !important;
}


.news-list-item-image,
.news-list-item-image-big,
.news-list-item-body {
  display: table-cell;
  vertical-align: top;
}
.news-list-item-image {
  width: 36px;
  font-size: 30px;
  text-align: center;
}

.news-list-item-image-big {
  width: 250px;
  font-size: 30px;
  text-align: center;
}
.news-list-item-body {
  padding-left: 20px;
}
.news-list-item-title {
  margin-top: 6px;
  display: block;
}
.news-list-item-title a{
  color: #333;
}
.news-list-item-title a:hover{
  color: #2a6496;
}
.news-list-item-title .pull-right{
  color: #777;
  font-size:11px;
  font-weight: normal;
}

.news-list-item-title2 {
  font-size: 13px;
  padding: 0px 10px;
  margin-top: 6px;
  display: block;
}
.news-list-item-title2 a{
  color: #333;
}
.news-list-item-title2 a:hover{
  color: #2a6496;
}

.news-list-item-title2 .pull-right{
  color: #777;
  font-size:11px;
  font-weight: normal;
}

.news-list-item-title3 {
  font-size: 14px;
  margin-top: 0px;
  margin-bottom: 8px;
  display: block;
}
.news-list-item-title3 a{
  color: #333;
}
.news-list-item-title3 a:hover{
  color: #2a6496;
}

.news-list-item-title3 .pull-right{
  color: #777;
  font-size:11px;
  font-weight: normal;
}


.news-list-item-time {
  margin-top: 6px;
  display: block;
  color: #777;
}

.news-list-item-time2 {

  display: block;
  color: #777;
}
.news-list-item-tags {
  margin-top: 6px;
  display: block;
  color: #777;

}

.news-list .pull-right button.btn-xs{font-weight: normal;font-size: 12px;}

.news-list .pull-right .dropdown-menu{font-size: 12px;}

.newlist_item_block h3{color:#2a6496;font-size: 14px; background: #f2f2f2; padding: 10px 15px; margin-bottom: 15px; }

.newlist_item_block h3 .pull-right{font-size: 12px; color: #666;font-weight: normal;}

.project_detail_block h3{color:#000;font-size: 14px; background: #f2f2f2; padding: 10px 15px; margin-bottom: 15px; }

.project_detail_block h3 .pull-right{font-size: 12px; color: #666;font-weight: normal;}
.project_detail_block h4{font-size: 14px;}
.project_detail_block h5{font-size: 12px;}

.heading{border-bottom: 1px dotted #ccc; padding-bottom: 8px;}

ul.others-news-list{list-style: none;padding: 0px; margin: 10px 0px;}
ul.others-news-list li{line-height: 20px;}
ul.others-news-list li a{color: #666;}
li.project-item{padding-top: 10px;}

li.project-item:nth-child(odd)
{
background:#f9f9f9;
}
li.project-item:nth-child(even)
{
background:#ffffff;
}

li.project-item2{padding: 20px 0px; }

li.project-item2:nth-child(odd)
{
background:#f9f9f9;
}
li.project-item2:nth-child(even)
{
background:#ffffff;
}

li.project-item3{padding: 10px 0px;  color: #777;}
li.project-item3 strong{margin-bottom: 6px;}
li.project-item3 strong a{ color: #333; font-size: 12px;}



a.tag{ display:inline-block; color: #777; padding-left:5px;}
a.tag:hover{color: #2a6496;}

.fav_remove_btn{color: #ccc; font-size: 11px;}

.color-up{ color: #2DAD38}
.color-down{ color: #AD2620}
.rank-list a{color: #333;}
.rank-list a:hover{color: #2a6496;}

#send_email_btn{margin-top: 10px;}

.index-table-1{ margin: 8px 0px 8px 0px;border-collapse:separate;border-spacing:10px 0px;}
.index-table-1 >tbody> tr > td{border:none; padding-left: 0px; padding-top: 2px; padding-bottom: 4px;}
.index-table-1 >tbody> tr.project-th > td{border-bottom:  1px solid #e1e1e1; padding-bottom: 2px;}


.map1{ background: url(../images/map.png) center center no-repeat; width: 400px; height: 195px; margin: 20px;}
.bs-glyphicons-list{ margin: 0; padding: 0;}
.bs-glyphicons-list li{ width: 80px; height: 100px; float: left; list-style: none;  margin: 10px;text-align: center;}
.bs-glyphicons-list li span:nth-child(1){font-size: 24px; display: block;  line-height: 24px; margin-bottom: 10px;}


.members-list{
  width: 100%;
  padding: 0px;
  margin: 0px;
  list-style: none;
  overflow: hidden;
}

.members-item{float: left;display: block; overflow: hidden; width: 80px;text-align: center; margin: 6px 12px; }

.members-item img.thumbnail{margin-bottom: 6px;}

.members-list-empty {
  padding: 25px 35px !important;
  text-align: center;
  clear: both;
}
.members-list-empty-title {
  color: #e74c3c;
}
.members-list-empty-text {
  color: #777;
}
.members-list-view-all {
  clear: both;
  text-align: center;
  margin-bottom: 0px;
  border-top: 1px dotted #ccc;
}
.members-list-view-all a{
  clear:both;
  padding: 8px 0px;
  font-size: 12px;
  white-space: normal;
  display: block;
  color: #333;
  text-decoration: none;
}

.members-list-view-all a:hover{
  color: #444;
  background: #eee;
}



.message-list{
  width: 100%;
  padding: 15px;
  margin: 0px;
  list-style: none;
  overflow: hidden;
}

.message-item{overflow: hidden; margin-bottom: 10px; border-top: 1px dotted #ccc; padding-top: 10px; }

.message-item:nth-child(1){padding-top: 10px; border-top: none;}
.message-item img.thumbnail{margin-bottom: 6px;}

.message-item-pic{float: left; margin-right: 20px;}

.message-list-empty {
  padding: 25px 35px !important;
  text-align: center;
  clear: both;
}
.message-list-empty-title {
  color: #e74c3c;
}
.message-list-empty-text {
  color: #777;
}
.message-list-view-all {
  clear: both;
  text-align: center;
  margin-bottom: 0px;
  border-top: 1px dotted #ccc;
}
.message-list-view-all a{
  clear:both;
  padding: 8px 0px;
  font-size: 12px;
  white-space: normal;
  display: block;
  color: #333;
  text-decoration: none;
}

.message-list-view-all a:hover{
  color: #444;
  background: #eee;
}
.message-time{color: #777;}
.panel-notop{border-top: none;}
.top_nav_pills li a{padding: 8px 15px; }

.big_list{padding: 15px;}

.preference_title{overflow: hidden;margin-top: 10px; background: #f2f2f2;  margin-bottom: 20px; padding: 0px 15px; border-top: 1px dotted #ccc;}
.preference_title h5{font-size: 12px; padding: 0px; }

.tag_block{margin-bottom: 10px;}
.no_border{border: none;}

.company_block{padding: 30px 15px 15px 15px;}
.company_block h1{font-size: 18px; margin-top: 0px;}
.company_block h3{font-size: 14px; margin-top: 0px;}
.company_logo{ margin-right: 15px; margin-bottom: 15px; width: 210px; height: 210px;}

.big_num{font-size: 24px; margin: 0px 4px; }
.green{color: #5cb85c}
.red{color: #e74c3c}
.blue{color: #428bca}

.new_detail_content{padding: 0px 15px; margin-bottom: 20px;}
.new_detail_content .news-list-item-time{padding-top: 0px; margin-bottom: 12px;}

#newchama_logo_main{width: 600px; margin: 0px auto 20px auto; padding-top: 20px; min-height: 400px; }
.reg-heading{border-bottom: 1px dotted #ccc; padding-bottom: 8px; margin: 20px 0px;font-size: 14px;}

.no-record-text{color: #777; text-align: center; margin: 0 auto 20px auto;}

.index_option_block{padding: 15px; background: #f9f9f9; margin-bottom: 8px;}

.new_detail_warpper{line-height: 1.6em;}
.new_detail_warpper img{margin: 10px auto;}
#map_dot_1{position: absolute; display: block; width: 80px; height: 80px; left: 45px; top: 57px;}
#map_dot_2{position: absolute; display: block; width: 80px; height: 80px; left: 306px; top: 65px;}
#map_btn_1{position: absolute; display: block; width: 80px; height: 80px; left: 45px; top: 57px;}
#map_btn_2{position: absolute; display: block; width: 80px; height: 80px; left: 306px; top: 65px; }

.chart-title{text-align: center; font-weight: bold;}
.chart_nav{text-align: center; margin: 15px auto; width: 80px; height: 12px; clear:both;}
.chart_nav a{background: url(../img/dot.png) 0px 0px no-repeat; width: 12px; height: 12px;display: block; margin: 0px 4px; float: left;}
.chart_nav a.on,.chart_nav a:hover{background-position: 0px -24px;}
.chart-loading{text-align: center; font-weight: bold; position: absolute; top: 50%; width: 100%;}


.float_usa{position: absolute; top: 82px; left: 94px; background: url(../img/arrow_left.png) 0px -5px no-repeat ; padding-left: 15px; width: 235px; height: 100px; display: none;}
.float_cn{position: absolute; top: 90px; left: 104px; background: url(../img/arrow_right.png) right -5px no-repeat ; padding-right: 15px; width: 235px; height: 100px; display: none; }

.float_block_title{background: #c1c1c1; border-radius: 4px 4px 0px 0px; width: 220px; height: 30px; line-height: 24px; color: #fff; padding: 4px 15px; }

.float_block_content{ border-bottom: 1px solid #c1c1c1; border-left: 1px solid #c1c1c1;border-right: 1px solid #c1c1c1; background: #fff; color: #333;width: 220px;  padding: 15px;border-radius:0px 0px 4px 4px ;  }
.float_block_content p{ margin-bottom: 6px;}

.float_usa .float_block_title{background: #006699;}
.float_cn .float_block_title{background: #cc6600;}

.see_more_btn{border-top: 1px dotted #ccc;}

.tag_cloud_block{ width: 100%; height: 240px; position: relative; overflow: hidden;}
.tag_cloud_block a{display: block; position: absolute; text-align: center; text-decoration: none; color: #fff; }
.tag_cloud_block a:hover{filter: alpha(opacity=60);
  -webkit-opacity: 0.6;
  -moz-opacity: 0.6;
  opacity: 0.6;}

.tag_cloud_block a#index_tag_1{width: 50%;height: 120px; top: 0px; left: 0px; background: #009dad;line-height: 120px;}
.tag_cloud_block a#index_tag_2{width: 50%;height: 60px; top: 0px; left: 50%; background: #b7542e;line-height: 60px;}
.tag_cloud_block a#index_tag_3{width: 25%;height: 60px; top: 60px; left: 50%; background: #e08f70;line-height: 60px;}
.tag_cloud_block a#index_tag_4{width: 25%;height: 60px; top: 60px; left: 75%; background: #1c2d47;line-height: 60px;}

.tag_cloud_block a#index_tag_5{width: 25%;height: 60px; top: 120px; left: 0%; background: #e08f70;line-height: 60px;}
.tag_cloud_block a#index_tag_6{width: 25%;height: 60px; top: 180px; left: 0%; background: #1c2d47;line-height: 60px;}
.tag_cloud_block a#index_tag_7{width: 25%;height: 120px; top: 120px; left: 25%; background: #b7542e;line-height: 120px;}


.tag_cloud_block a#index_tag_8{width: 12.5%;height: 30px; top: 120px; left: 50%; background: #009dad;line-height: 30px;}
.tag_cloud_block a#index_tag_9{width: 12.5%;height: 30px; top: 120px; left: 62.5%; background: #46c7d4;line-height: 30px;}
.tag_cloud_block a#index_tag_10{width: 12.5%;height: 30px; top: 120px; left: 75%; background: #009dad;line-height: 30px;}
.tag_cloud_block a#index_tag_11{width: 12.5%;height: 30px; top: 120px; left: 87.5%; background: #46c7d4;line-height: 30px;}

.tag_cloud_block a#index_tag_12{width: 25%;height: 90px; top: 150px; left: 50%; background: #e08f70;line-height: 90px;}
.tag_cloud_block a#index_tag_13{width: 25%;height: 45px; top: 150px; left: 75%; background: #1c2d47;line-height: 45px;}
.tag_cloud_block a#index_tag_14{width: 25%;height: 45px; top: 195px; left: 75%; background: #46c7d4;line-height: 45px;}

.index_top_num{margin: 0px 10px;}
.members-list {overflow: hidden;position: relative;}
.members-list .members-item {overflow: hidden; position: relative;}
.members-list .members-item .badge{
  position: absolute;
    top: 0px;
    right: 5px;
    border-top-right-radius: 100px;
    border-top-left-radius: 100px;
    border-bottom-right-radius: 100px;
    border-bottom-left-radius: 100px;
      padding-top: 4px;
  padding-bottom: 4px;
  font-size: 10px;
  background: #e74c3c;
  border: 2px solid #e74c3c;
}

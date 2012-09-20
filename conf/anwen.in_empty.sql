/*
Navicat MySQL Data Transfer

Source Server         : libolocal
Source Server Version : 50516
Source Host           : localhost:3306
Source Database       : anwen.in

Target Server Type    : MYSQL
Target Server Version : 50516
File Encoding         : 65001

Date: 2012-09-18 20:30:26
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `ande`
-- ----------------------------
DROP TABLE IF EXISTS `ande`;
CREATE TABLE `ande` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `usersay` varchar(512) NOT NULL,
  `andesay` mediumtext NOT NULL,
  `chattime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ande
-- ----------------------------

-- ----------------------------
-- Table structure for `comments`
-- ----------------------------
DROP TABLE IF EXISTS `comments`;
CREATE TABLE `comments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `author_id` int(11) NOT NULL,
  `share_id` int(11) NOT NULL DEFAULT '0',
  `commentbody` mediumtext NOT NULL,
  `commenttime` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `published` (`commenttime`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of comments
-- ----------------------------

-- ----------------------------
-- Table structure for `likes`
-- ----------------------------
DROP TABLE IF EXISTS `likes`;
CREATE TABLE `likes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `share_id` int(11) NOT NULL DEFAULT '0',
  `liketime` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `published` (`liketime`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of likes
-- ----------------------------

-- ----------------------------
-- Table structure for `shares`
-- ----------------------------
DROP TABLE IF EXISTS `shares`;
CREATE TABLE `shares` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `author_id` int(11) NOT NULL,
  `title` varchar(512) NOT NULL,
  `sharetype` varchar(20) NOT NULL DEFAULT 'pencil',
  `markdown` mediumtext NOT NULL,
  `html` mediumtext NOT NULL,
  `published` datetime NOT NULL,
  `commentnum` int(11) NOT NULL DEFAULT '0',
  `updated` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `likes` int(11) NOT NULL DEFAULT '0',
  `hits` int(11) NOT NULL DEFAULT '0',
  `slug` varchar(20) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`,`likes`),
  KEY `published` (`published`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of shares
-- ----------------------------

-- ----------------------------
-- Table structure for `users`
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `user_id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `user_name` varchar(60) NOT NULL DEFAULT '',
  `user_pass` varchar(64) NOT NULL DEFAULT '',
  `user_email` varchar(100) NOT NULL DEFAULT '',
  `user_say` mediumtext,
  `user_leaf` int(11) NOT NULL DEFAULT '0',
  `user_domain` varchar(20) NOT NULL,
  `user_url` varchar(100) NOT NULL DEFAULT '',
  `user_registered` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_activation_key` varchar(60) NOT NULL DEFAULT '',
  `user_status` int(11) NOT NULL DEFAULT '0',
  `user_city` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  KEY `user_name` (`user_name`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of users
-- ----------------------------

-- phpMyAdmin SQL Dump
-- version 4.8.4
-- https://www.phpmyadmin.net/
--
-- Anamakine: 127.0.0.1:3306
-- Üretim Zamanı: 26 May 2019, 11:24:49
-- Sunucu sürümü: 5.7.24
-- PHP Sürümü: 7.2.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Veritabanı: `rasp_prj`
--

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `rasp_commands`
--

DROP TABLE IF EXISTS `rasp_commands`;
CREATE TABLE IF NOT EXISTS `rasp_commands` (
  `led_red` varchar(256) COLLATE utf8_unicode_ci NOT NULL,
  `led_green` varchar(256) COLLATE utf8_unicode_ci NOT NULL,
  `led_blue` varchar(256) COLLATE utf8_unicode_ci NOT NULL,
  `motor_direction` varchar(256) COLLATE utf8_unicode_ci NOT NULL,
  `motor_speed` varchar(256) COLLATE utf8_unicode_ci NOT NULL,
  `motor_steps` varchar(256) COLLATE utf8_unicode_ci NOT NULL,
  `motor_start_stop` varchar(256) COLLATE utf8_unicode_ci NOT NULL,
  `res_1` varchar(256) COLLATE utf8_unicode_ci NOT NULL,
  `res_2` varchar(256) COLLATE utf8_unicode_ci NOT NULL,
  `res_3` varchar(256) COLLATE utf8_unicode_ci NOT NULL,
  `res_4` varchar(256) COLLATE utf8_unicode_ci NOT NULL,
  `res_5` varchar(256) COLLATE utf8_unicode_ci NOT NULL,
  `res_6` varchar(256) COLLATE utf8_unicode_ci NOT NULL,
  `res_7` varchar(256) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Tablo döküm verisi `rasp_commands`
--

INSERT INTO `rasp_commands` (`led_red`, `led_green`, `led_blue`, `motor_direction`, `motor_speed`, `motor_steps`, `motor_start_stop`, `res_1`, `res_2`, `res_3`, `res_4`, `res_5`, `res_6`, `res_7`) VALUES
('off', 'off', 'off', 'forward', '99', '50000000', 'disable', 'reserved', 'reserved', 'reserved', 'reserved', 'reserved', 'reserved', 'reserved');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `rasp_status`
--

DROP TABLE IF EXISTS `rasp_status`;
CREATE TABLE IF NOT EXISTS `rasp_status` (
  `weight` varchar(256) COLLATE utf8_unicode_ci NOT NULL,
  `motor_cur_pos` varchar(256) COLLATE utf8_unicode_ci NOT NULL,
  `motor_is_en_dis` varchar(256) COLLATE utf8_unicode_ci NOT NULL,
  `motor_speed` varchar(256) COLLATE utf8_unicode_ci NOT NULL,
  `res_2` varchar(256) COLLATE utf8_unicode_ci NOT NULL,
  `res_3` varchar(256) COLLATE utf8_unicode_ci NOT NULL,
  `res_4` varchar(256) COLLATE utf8_unicode_ci NOT NULL,
  `res_5` varchar(256) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Tablo döküm verisi `rasp_status`
--

INSERT INTO `rasp_status` (`weight`, `motor_cur_pos`, `motor_is_en_dis`, `motor_speed`, `res_2`, `res_3`, `res_4`, `res_5`) VALUES
('off', '-14765', 'disabled', '99', 'reserved', 'reserved', 'reserved', 'reserved');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

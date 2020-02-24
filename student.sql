-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 20, 2019 at 07:36 AM
-- Server version: 10.4.10-MariaDB
-- PHP Version: 7.1.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `student_management_system`
--

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `First_Name` varchar(20) NOT NULL,
  `Last_Name` varchar(20) NOT NULL,
  `Student_Id` int(20) NOT NULL,
  `DOB` varchar(20) NOT NULL,
  `Gender` varchar(20) NOT NULL,
  `Roll_No` int(20) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `Phone_No` varchar(50) DEFAULT NULL,
  `Address` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`First_Name`, `Last_Name`, `Student_Id`, `DOB`, `Gender`, `Roll_No`, `Email`, `Phone_No`, `Address`) VALUES
('arshina', 'Dange', 3117008, '26-12-1999', 'Female', 8, 'xyz@gmail.com', '2147483647', 'abc\n'),
('Mohd', 'Khan', 3117020, '06-11-1999', 'Male', 20, 'abc@gmail.com', '123456789', 'xyz\n'),
('abdullah', 'shaikh', 3117047, '17-12-1999', 'Male', 47, 'ok@gmail.com', '2147483647', 'bhindi bazaar\n'),
('Hamza', 'Chowdhury', 6117011, '23-03-1999', 'Male', 11, 'hamza@gmail.com', '2147483647', '123 Bhindi Bazaar,abc street,room no:57,8th floor,');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`Student_Id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

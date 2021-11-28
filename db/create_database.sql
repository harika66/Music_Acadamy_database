

--
-- Create database Student
--

DROP SCHEMA IF EXISTS `Student` ;
CREATE SCHEMA IF NOT EXISTS `Student` DEFAULT CHARACTER SET utf8 ;
USE `Student` ;

--
-- Table structure for table `student_info`
--

DROP TABLE IF EXISTS `student_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student_info` (
  `std_id` int NOT NULL AUTO_INCREMENT,
  `std_name` varchar(100) DEFAULT NULL,
  `course_name` varchar(100) DEFAULT NULL,
  `batch` varchar(25) DEFAULT NULL,
  `tch_name` varchar(100) DEFAULT NULL,
  `fees` int DEFAULT NULL,
  PRIMARY KEY (`std_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;


-- Dump completed on 2021-11-18 18:11:03

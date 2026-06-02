-- MySQL dump 10.13  Distrib 8.0.42, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: mydb
-- ------------------------------------------------------
-- Server version	9.3.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `categor`
--

DROP TABLE IF EXISTS `categor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categor` (
  `id_categor` int NOT NULL AUTO_INCREMENT,
  `categor_name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_categor`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categor`
--

LOCK TABLES `categor` WRITE;
/*!40000 ALTER TABLE `categor` DISABLE KEYS */;
INSERT INTO `categor` VALUES (1,'Женская обувь'),(2,'Мужская обувь');
/*!40000 ALTER TABLE `categor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `enum`
--

DROP TABLE IF EXISTS `enum`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `enum` (
  `id_enum` int NOT NULL,
  `enum_name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_enum`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `enum`
--

LOCK TABLES `enum` WRITE;
/*!40000 ALTER TABLE `enum` DISABLE KEYS */;
INSERT INTO `enum` VALUES (1,'шт');
/*!40000 ALTER TABLE `enum` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `point`
--

DROP TABLE IF EXISTS `point`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `point` (
  `id_point` int NOT NULL AUTO_INCREMENT,
  `inn` int DEFAULT NULL,
  `city` varchar(45) DEFAULT NULL,
  `street` varchar(45) DEFAULT NULL,
  `home` int DEFAULT NULL,
  PRIMARY KEY (`id_point`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `point`
--

LOCK TABLES `point` WRITE;
/*!40000 ALTER TABLE `point` DISABLE KEYS */;
INSERT INTO `point` VALUES (1,420151,'Лесной','Вишневая',32),(2,125061,'Лесной','Подгорная',8),(3,630370,'Лесной','Шоссейная',24),(4,400562,'Лесной','Зеленая',32),(5,614510,'Лесной','Маяковского',47),(6,410542,'Лесной','Светлая',46),(7,620839,'Лесной','Цветочная',8),(8,443890,'Лесной','Коммунистическая',1),(9,603379,'Лесной','Спортивная',46),(10,603721,'Лесной','Гоголя',41),(11,410172,'Лесной','Северная',13),(12,614611,'Лесной','Молодежная',50),(13,454311,'Лесной','Новая',19),(14,660007,'Лесной','Октябрьская',19),(15,603036,'Лесной','Садовая',4),(16,394060,'Лесной','Фрунзе',43),(17,410661,'Лесной','Школьная',50),(18,625590,'Лесной','Коммунистическая',20),(19,625683,'Лесной','8 Марта',0),(20,450983,'Лесной','Комсомольская',26),(21,394782,'Лесной','Чехова',3),(22,603002,'Лесной','Дзержинского',28),(23,450558,'Лесной','Набережная',30),(24,344288,'Лесной','Чехова',1),(25,614164,'Лесной','   Степная',30),(26,394242,'Лесной','Коммунистическая',43),(27,660540,'Лесной','Солнечная',25),(28,125837,'Лесной','Шоссейная',40),(29,125703,'Лесной','Партизанская',49),(30,625283,'Лесной','Победы',46),(31,614753,'Лесной','Полевая',35),(32,426030,'Лесной','Маяковского',44),(33,450375,'Лесной','Клубная',44),(34,625560,'Лесной','Некрасова',12),(35,630201,'Лесной','Комсомольская',17),(36,190949,'Лесной','Мичурина',26);
/*!40000 ALTER TABLE `point` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `postav`
--

DROP TABLE IF EXISTS `postav`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `postav` (
  `id_postav` int NOT NULL AUTO_INCREMENT,
  `postav_name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_postav`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `postav`
--

LOCK TABLES `postav` WRITE;
/*!40000 ALTER TABLE `postav` DISABLE KEYS */;
INSERT INTO `postav` VALUES (1,'Kari'),(2,'Обувь для вас');
/*!40000 ALTER TABLE `postav` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `productinorder`
--

DROP TABLE IF EXISTS `productinorder`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `productinorder` (
  `id_productinorder` int NOT NULL AUTO_INCREMENT,
  `id_tovar` int DEFAULT NULL,
  `id_zakaz` int DEFAULT NULL,
  `kol` int DEFAULT NULL,
  PRIMARY KEY (`id_productinorder`),
  KEY `8_idx` (`id_zakaz`),
  KEY `9_idx` (`id_tovar`),
  CONSTRAINT `8` FOREIGN KEY (`id_zakaz`) REFERENCES `zakaz` (`id_zakaz`),
  CONSTRAINT `9` FOREIGN KEY (`id_tovar`) REFERENCES `tovar` (`id_tovar`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `productinorder`
--

LOCK TABLES `productinorder` WRITE;
/*!40000 ALTER TABLE `productinorder` DISABLE KEYS */;
INSERT INTO `productinorder` VALUES (1,1,1,2),(2,2,3,1),(3,3,5,10),(4,4,7,5),(5,5,1,2),(6,6,3,1),(7,7,5,10),(8,8,7,5),(9,9,9,5),(10,10,11,5),(11,11,2,2),(12,12,4,1),(13,13,6,10),(14,14,8,4),(15,15,2,2),(16,16,4,1),(17,17,6,10),(18,18,8,4),(19,19,10,1),(20,20,12,5);
/*!40000 ALTER TABLE `productinorder` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proizvod`
--

DROP TABLE IF EXISTS `proizvod`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proizvod` (
  `id_proizvod` int NOT NULL AUTO_INCREMENT,
  `proizvod_name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_proizvod`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proizvod`
--

LOCK TABLES `proizvod` WRITE;
/*!40000 ALTER TABLE `proizvod` DISABLE KEYS */;
INSERT INTO `proizvod` VALUES (1,'Kari'),(2,'Marco Tozzi'),(3,'Рос'),(4,'Rieker'),(5,'Alessio Nesca'),(6,'CROSBY');
/*!40000 ALTER TABLE `proizvod` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `role`
--

DROP TABLE IF EXISTS `role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `role` (
  `id_role` int NOT NULL AUTO_INCREMENT,
  `role_name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_role`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `role`
--

LOCK TABLES `role` WRITE;
/*!40000 ALTER TABLE `role` DISABLE KEYS */;
INSERT INTO `role` VALUES (1,'Администратор'),(2,'Менеджер'),(3,'Авторизированный клиент');
/*!40000 ALTER TABLE `role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `status`
--

DROP TABLE IF EXISTS `status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `status` (
  `id_status` int NOT NULL AUTO_INCREMENT,
  `status_name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_status`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `status`
--

LOCK TABLES `status` WRITE;
/*!40000 ALTER TABLE `status` DISABLE KEYS */;
INSERT INTO `status` VALUES (1,'Завершен'),(2,'Новый');
/*!40000 ALTER TABLE `status` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tovar`
--

DROP TABLE IF EXISTS `tovar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tovar` (
  `id_tovar` int NOT NULL AUTO_INCREMENT,
  `art` varchar(45) DEFAULT NULL,
  `tovar_name` varchar(45) DEFAULT NULL,
  `price` int DEFAULT NULL,
  `sale` int DEFAULT NULL,
  `kol_sklad` int DEFAULT NULL,
  `opisanie` varchar(405) DEFAULT NULL,
  `foto` varchar(45) DEFAULT NULL,
  `id_postav` int DEFAULT NULL,
  `id_proizvod` int DEFAULT NULL,
  `id_categor` int DEFAULT NULL,
  `id_enum` int DEFAULT NULL,
  PRIMARY KEY (`id_tovar`),
  KEY `1_idx` (`id_categor`),
  KEY `2_idx` (`id_enum`),
  KEY `3_idx` (`id_postav`),
  KEY `4_idx` (`id_proizvod`),
  CONSTRAINT `1` FOREIGN KEY (`id_categor`) REFERENCES `categor` (`id_categor`),
  CONSTRAINT `2` FOREIGN KEY (`id_enum`) REFERENCES `enum` (`id_enum`),
  CONSTRAINT `3` FOREIGN KEY (`id_postav`) REFERENCES `postav` (`id_postav`),
  CONSTRAINT `4` FOREIGN KEY (`id_proizvod`) REFERENCES `proizvod` (`id_proizvod`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tovar`
--

LOCK TABLES `tovar` WRITE;
/*!40000 ALTER TABLE `tovar` DISABLE KEYS */;
INSERT INTO `tovar` VALUES (1,'А112Т4','Ботинки',4990,3,6,'Женские Ботинки демисезонные kari','Image/1.jpg',1,1,1,1),(2,'F635R4','Ботинки',3244,2,13,'Ботинки Marco Tozzi женские демисезонные, размер 39, цвет бежевый','Image/2.jpg',2,2,1,1),(3,'H782T5','Туфли',4499,4,5,'Туфли kari мужские классика MYZ21AW-450A, размер 43, цвет: черный','Image/3.jpg',1,1,2,1),(4,'G783F5','Ботинки',5900,2,8,'Мужские ботинки Рос-Обувь кожаные с натуральным мехом','Image/4.jpg',1,3,2,1),(5,'J384T6','Ботинки',3800,2,16,'B3430/14 Полуботинки мужские Rieker','Image/5.jpg',2,4,2,1),(6,'D572U8','Кроссовки',4100,3,6,'129615-4 Кроссовки мужские','Image/6.jpg',2,3,2,1),(7,'F572H7','Туфли',2700,2,14,'Туфли Marco Tozzi женские летние, размер 39, цвет черный','Image/7.jpg',1,2,1,1),(8,'D329H3','Полуботинки',1890,4,4,'Полуботинки Alessio Nesca женские 3-30797-47, размер 37, цвет: бордовый','Image/8.jpg',2,5,1,1),(9,'B320R5','Туфли',4300,2,6,'Туфли Rieker женские демисезонные, размер 41, цвет коричневый','Image/9.jpg',1,4,1,1),(10,'G432E4','Туфли',2800,3,15,'Туфли kari женские TR-YR-413017, размер 37, цвет: черный','Image/10.jpg',1,1,1,1),(11,'S213E3','Полуботинки',2156,3,6,'407700/01-01 Полуботинки мужские CROSBY','Image/picture.png',2,6,2,1),(12,'E482R4','Полуботинки',1800,2,14,'Полуботинки kari женские MYZ20S-149, размер 41, цвет: черный','Image/picture.png',1,1,1,1),(13,'S634B5','Кеды',5500,3,0,'Кеды Caprice мужские демисезонные, размер 42, цвет черный','Image/picture.png',2,6,2,1),(14,'K345R4','Полуботинки',2100,2,3,'407700/01-02 Полуботинки мужские CROSBY','Image/picture.png',2,6,2,1),(15,'O754F4','Туфли',5400,4,18,'Туфли женские демисезонные Rieker артикул 55073-68/37','Image/picture.png',2,4,1,1),(16,'G531F4','Ботинки',6600,12,9,'Ботинки женские зимние ROMER арт. 893167-01 Черный','Image/picture.png',1,1,1,1),(17,'J542F5','Тапочки',500,13,0,'Тапочки мужские Арт.70701-55-67син р.41','Image/picture.png',1,1,2,1),(18,'B431R5','Ботинки',2700,2,5,'Мужские кожаные ботинки/мужские ботинки','Image/picture.png',2,4,2,1),(19,'P764G4','Туфли',6800,15,15,'Туфли женские, ARGO, размер 38','Image/picture.png',1,6,1,1),(20,'C436G5','Ботинки',10200,15,9,'Ботинки женские, ARGO, размер 40','Image/picture.png',1,5,1,1),(21,'F427R5','Ботинки',11800,15,11,'Ботинки на молнии с декоративной пряжкой FRAU','Image/picture.png',2,4,1,1),(22,'N457T5','Полуботинки',4600,3,13,'Полуботинки Ботинки черные зимние, мех','Image/picture.png',1,6,1,1),(23,'D364R4','Туфли',12400,16,5,'Туфли Luiza Belly женские Kate-lazo черные из натуральной замши','Image/picture.png',1,1,1,1),(24,'S326R5','Тапочки',9900,17,15,'Мужские кожаные тапочки \"Профиль С.Дали\" ','Image/picture.png',2,6,2,1),(25,'L754R4','Полуботинки',1700,2,7,'Полуботинки kari женские WB2020SS-26, размер 38, цвет: черный','Image/picture.png',1,1,1,1),(26,'M542T5','Кроссовки',2800,18,3,'Кроссовки мужские TOFA','Image/picture.png',2,4,2,1),(27,'D268G5','Туфли',4399,3,12,'Туфли Rieker женские демисезонные, размер 36, цвет коричневый','Image/picture.png',2,4,1,1),(28,'T324F5','Сапоги',4699,2,5,'Сапоги замша Цвет: синий','Image/picture.png',1,6,1,1),(29,'K358H6','Тапочки',599,20,2,'Тапочки мужские син р.41','Image/picture.png',1,4,2,1),(30,'H535R5','Ботинки',2300,2,7,'Женские Ботинки демисезонные','Image/picture.png',2,1,1,1);
/*!40000 ALTER TABLE `tovar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id_user` int NOT NULL AUTO_INCREMENT,
  `familia` varchar(45) DEFAULT NULL,
  `name` varchar(45) DEFAULT NULL,
  `otchestvo` varchar(45) DEFAULT NULL,
  `login` varchar(70) DEFAULT NULL,
  `password` varchar(45) DEFAULT NULL,
  `id_role` int DEFAULT NULL,
  PRIMARY KEY (`id_user`),
  KEY `7_idx` (`id_role`),
  CONSTRAINT `7` FOREIGN KEY (`id_role`) REFERENCES `role` (`id_role`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'Никифорова','Весения','Николаевна','94d5ous@gmail.com','uzWC67',1),(2,'Сазонов','Руслан','Германович','uth4iz@mail.com','2L6KZG',1),(3,'Одинцов','Серафим','Артёмович','yzls62@outlook.com','JlFRCZ',1),(4,'Степанов','Михаил','Артёмович','1diph5e@tutanota.com','8ntwUp',2),(5,'Ворсин','Петр','Евгеньевич','tjde7c@yahoo.com','YOyhfR',2),(6,'Старикова','Елена','Павловна','wpmrc3do@tutanota.com','RSbvHv',2),(7,'Михайлюк','Анна','Вячеславовна','5d4zbu@tutanota.com','rwVDh9',3),(8,'Ситдикова','Елена','Анатольевна','ptec8ym@yahoo.com','LdNyos',3),(9,'Ворсин','Петр','Евгеньевич','1qz4kw@mail.com','gynQMT',3),(10,'Старикова','Елена','Павловна','4np6se@mail.com','AtnDjr',3);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `zakaz`
--

DROP TABLE IF EXISTS `zakaz`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `zakaz` (
  `id_zakaz` int NOT NULL AUTO_INCREMENT,
  `data_zakaz` date DEFAULT NULL,
  `data_pos` date DEFAULT NULL,
  `kod` int DEFAULT NULL,
  `id_status` int DEFAULT NULL,
  `id_point` int DEFAULT NULL,
  `id_user` int DEFAULT NULL,
  PRIMARY KEY (`id_zakaz`),
  KEY `5_idx` (`id_point`),
  KEY `6_idx` (`id_status`),
  KEY `10_idx` (`id_user`),
  CONSTRAINT `10` FOREIGN KEY (`id_user`) REFERENCES `user` (`id_user`),
  CONSTRAINT `5` FOREIGN KEY (`id_point`) REFERENCES `point` (`id_point`),
  CONSTRAINT `6` FOREIGN KEY (`id_status`) REFERENCES `status` (`id_status`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `zakaz`
--

LOCK TABLES `zakaz` WRITE;
/*!40000 ALTER TABLE `zakaz` DISABLE KEYS */;
INSERT INTO `zakaz` VALUES (1,'2025-02-27','2025-04-20',901,1,1,4),(2,'2022-09-28','2025-04-21',902,1,11,1),(3,'2025-03-21','2025-04-22',903,1,2,2),(4,'2025-02-20','2025-04-23',904,1,11,3),(5,'2025-03-17','2025-04-24',905,1,2,4),(6,'2025-03-01','2025-04-25',906,1,15,1),(7,'2025-02-27','2025-04-26',907,1,3,2),(8,'2025-03-31','2025-04-27',908,2,19,3),(9,'2025-04-02','2025-04-28',909,2,5,4),(10,'2025-04-03','2025-04-29',910,2,19,4),(11,'2025-02-27','2025-04-20',901,1,1,4),(12,'2022-09-28','2025-04-21',902,1,11,1),(13,'2025-03-21','2025-04-22',903,1,2,2),(14,'2025-02-20','2025-04-23',904,1,11,3),(15,'2025-03-17','2025-04-24',905,1,2,4),(16,'2025-03-01','2025-04-25',906,1,15,1),(17,'2025-02-27','2025-04-26',907,1,3,2),(18,'2025-03-31','2025-04-27',908,2,19,3),(19,'2025-04-02','2025-04-28',909,2,5,4),(20,'2025-04-03','2025-04-29',910,2,19,4);
/*!40000 ALTER TABLE `zakaz` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-06-01 23:06:50

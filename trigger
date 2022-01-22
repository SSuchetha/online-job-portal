CREATE DEFINER=`root`@`localhost` TRIGGER `job_portal`.`user_AFTER_INSERT` AFTER INSERT ON `user` FOR EACH ROW
BEGIN
	insert into transaction values(curdate(),curtime());
END

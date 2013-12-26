CREATE TABLE `test_%s` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `name` varchar(255) NOT NULL,
    `data` text NOT NULL,
    `created` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
    `updated` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    `status` tinyint NOT NULL DEFAULT 1,
    PRIMARY KEY (`id`),
    KEY `name` (`name`(16)),
    KEY `created` (`created`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

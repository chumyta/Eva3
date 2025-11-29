USE log;

CREATE TABLE log (
    id INT AUTO_INCREMENT PRIMARY KEY,
    hora DATETIME,
    actividad VARCHAR(255),
    estado VARCHAR(255),
    imagen VARCHAR(255)
);

INSERT INTO log (hora, actividad, estado, imagen) 
VALUES ('2025-11-29 10:07', 'Inicio del sistema', 'Error, Pusimos el puerto 5000', 'image2.png');

INSERT INTO log (hora, actividad, estado, imagen) 
VALUES ('2025-11-29 10:08', 'Inicio del sistema', 'Solucionado, Era el puerto 8080', 'image3.png');

INSERT INTO log (hora, actividad, estado, imagen) 
VALUES ('2025-11-29 10:07', 'Permisos de DB', 'Error, Pusimos mal los permisos', 'image.png');

INSERT INTO log (hora, actividad, estado, imagen) 
VALUES ('2025-11-29 10:07', 'Permisos de DB', 'Solucionado, Le dimos bien los permisos', 'image4.png');

INSERT INTO log (hora, actividad, estado, imagen) 
VALUES ('2025-11-29 13:20', 'Conexión a BD', 'Exitoso', 'logo.jpg');


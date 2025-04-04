<?php
$dsn = 'pgsql:host=localhost;port=5432;dbname=phpapp';
$username = 'postgres';
$password = 'postgres';

// Options for error handling and fetching modes
$options = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION, // Throw exceptions on errors
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC, // Fetch associative arrays
];

try {
    // Create a PDO instance (connect to the database)
    $pdo = new PDO($dsn, $username, $password, $options);
    echo "Connected successfully!";
    
} catch (PDOException $e) {
    // Handle connection errors
    echo "Connection failed: " . $e->getMessage(). "<br>";
    
}
?>

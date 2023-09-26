<!DOCTYPE html>
<html>
<head>
  <title>Air Mouse</title>
</head>
<body>

<h1>Air Mouse</h1>

<p>This repository contains the source code and documentation for the <strong>Air Mouse</strong>. It allows you to control your computer's mouse cursor using an MPU6050 gyroscope and accelerometer sensor connected to an Arduino. The Arduino reads sensor data and sends it via the serial port to a Python program that translates the data into mouse movements on the screen.
</p>

<h2>Requirements</h2>

<ul>
  <li><strong>Hardware</strong>: Arduino board, MPU6050 sensor, USB cable.</li>
  <li><strong>Software</strong>: Arduino IDE, Python 3.x, and Python libraries (<code>pyserial</code>, <code>pyautogui</code>).</li>
</ul>

<h2>Setup</h2>

<ol>
  <li><strong>Connect Hardware</strong>: Wire the MPU6050 to your Arduino following documentation.</li>
  <li><strong>Upload Arduino Sketch</strong>: Load and upload <code>arduino_mpu6050.ino</code> from this repo to your Arduino.</li>
  <li><strong>Install Python Dependencies</strong>: In the <code>python</code> directory, run:
    <pre><code>pip install pyserial pyautogui</code></pre>
  </li>
</ol>

<h2>Usage</h2>

<ol>
  <li><strong>Connect Arduino</strong>: Plug your Arduino into your computer.</li>
  <li><strong>Run Python Program</strong>: In the <code>python</code> directory, run:
    <pre><code>python air_mouse.py</code></pre>
  </li>
  <li><strong>Control the Mouse</strong>: Tilt and move the sensor to control the cursor.</li>
</ol>
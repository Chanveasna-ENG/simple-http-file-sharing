# File Sharing Application

## Setup

To set up the application for the first time, run the following command:

```bat
setup.bat
```

This will create a virtual environment, install Django, run migrations, and prompt you to create a superuser.

## Running the Server

To run the server, use the following command:

```bat
"Share File.bat"
```

This will check if the virtual environment exists and run the setup if necessary, then start the Django development server.

## Accessing the Application

After setting up, you can access the admin interface and approve devices using the following URLs:

```plaintext
Admin interface: http://127.0.0.1:10000/admin/
Approve devices: http://127.0.0.1:10000/admin/files/approveddevice/
```

To access the device, use the following URL in your web browser:

```plaintext
your_ip_address:10000
```

Make sure to run the server locally only. Do not expose the server to the internet.

Ask for approval from the admin to access the device.

Then you can access the device using this link:

```plaintext
your_ip_address:10000
```

## Stopping the Server

To stop the server, press `Ctrl+C` in the terminal where the server is running.
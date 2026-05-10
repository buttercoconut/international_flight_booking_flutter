import 'package:flutter/material.dart';
import '../services/api_service.dart';

class BookingScreen extends StatefulWidget {
  final dynamic flight;
  BookingScreen({required this.flight});

  @override
  _BookingScreenState createState() => _BookingScreenState();
}

class _BookingScreenState extends State<BookingScreen> {
  bool _bookingSuccess = false;

  void _book() async {
    final response = await ApiService.bookFlight(widget.flight['flight_id']);
    setState(() {
      _bookingSuccess = true;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Book Flight')),
      body: Center(
        child: _bookingSuccess
            ? Text('Booking Confirmed!')
            : ElevatedButton(
                onPressed: _book,
                child: Text('Confirm Booking'),
              ),
      ),
    );
  }
}

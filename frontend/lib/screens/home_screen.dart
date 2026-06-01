import 'package:flutter/material.dart';
import 'package:international_flight_booking/widgets/search_form.dart';

class HomeScreen extends StatelessWidget {
  static const routeName = '/';

  const HomeScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Flight Booking'),
      ),
      body: const Padding(
        padding: EdgeInsets.all(16.0),
        child: SearchForm(),
      ),
    );
  }
}

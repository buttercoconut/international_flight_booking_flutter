import 'package:flutter/material.dart';
import 'package:international_flight_booking/widgets/flight_card.dart';
import 'package:international_flight_booking/services/api_service.dart';
import 'package:provider/provider.dart';

class FlightComparisonScreen extends StatelessWidget {
  const FlightComparisonScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    // For simplicity, this screen just shows a placeholder.
    return Scaffold(
      appBar: AppBar(
        title: const Text('Compare Flights'),
      ),
      body: const Center(
        child: Text('Flight comparison feature coming soon!'),
      ),
    );
  }
}

import 'package:flutter/material.dart';
import '../widgets/flight_card.dart';
import '../services/api_service.dart';
import '../models/flight.dart';

class FlightSearchScreen extends StatefulWidget {
  const FlightSearchScreen({Key? key}) : super(key: key);

  @override
  _FlightSearchScreenState createState() => _FlightSearchScreenState();
}

class _FlightSearchScreenState extends State<FlightSearchScreen> {
  final ApiService _apiService = ApiService();
  List<Flight> _flights = [];
  bool _isLoading = false;

  @override
  void initState() {
    super.initState();
    _searchFlights();
  }

  Future<void> _searchFlights() async {
    setState(() => _isLoading = true);
    final flights = await _apiService.searchFlights(
      origin: 'NYC',
      destination: 'LHR',
      date: DateTime.now().add(const Duration(days: 7)),
      passengers: 1,
    );
    setState(() {
      _flights = flights;
      _isLoading = false;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Search Flights'),
      ),
      body: _isLoading
          ? const Center(child: CircularProgressIndicator())
          : ListView.builder(
              itemCount: _flights.length,
              itemBuilder: (context, index) {
                return FlightCard(flight: _flights[index]);
              },
            ),
    );
  }
}

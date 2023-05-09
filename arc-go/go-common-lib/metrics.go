package common

type Counter interface {
	Inc()
}

type CounterWithLabels interface {
	With(map[string]string) Counter
}

type MetricsStore interface {
	NewCounter(name string) Counter
	NewCounterWithLabels(name string, labels []string) CounterWithLabels
}

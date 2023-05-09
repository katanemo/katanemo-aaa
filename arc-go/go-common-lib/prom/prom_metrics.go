package prom

import (
	"github.com/katanemo/katanemo-aaa/arc-go/go-common-lib"
	"github.com/prometheus/client_golang/prometheus"
)

type promMetrics struct {
	registerer prometheus.Registerer
}

type promCounter struct {
	counter prometheus.Counter
}

// Inc implements common.Counter
func (c *promCounter) Inc() {
	c.counter.Inc()
}

type promCounterWithLabel struct {
	counterWithLabel *prometheus.CounterVec
}

// Inc implements common.Counter
func (c *promCounterWithLabel) With(labels map[string]string) common.Counter {
	return &promCounter{
		counter: c.counterWithLabel.With(labels),
	}
}

func (p *promMetrics) NewCounterWithLabels(name string, labels []string) common.CounterWithLabels {
	counter := prometheus.NewCounterVec(prometheus.CounterOpts{
		Name: name,
	}, labels)
	p.registerer.MustRegister(counter)
	return &promCounterWithLabel{
		counterWithLabel: counter,
	}
}

func (p *promMetrics) NewCounter(name string) common.Counter {
	counter := prometheus.NewCounter(prometheus.CounterOpts{
		Name: name,
	})
	p.registerer.MustRegister(counter)
	return &promCounter{
		counter: counter,
	}
}

func MetricsStore(registerer prometheus.Registerer) common.MetricsStore {
	return &promMetrics{
		registerer: registerer,
	}
}

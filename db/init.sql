
CREATE TABLE order_events (
    event_id UUID PRIMARY KEY NOT NULL,
    event_type VARCHAR(50) NOT NULL,
    order_id VARCHAR(50) NOT NULL,
    warehouse_id VARCHAR(50) NOT NULL,
    sku_id VARCHAR(50) NOT NULL,
    quantity INTEGER NOT NULL,
    amount NUMERIC(10,2) NOT NULL,
    status VARCHAR(30) NOT NULL,
    event_timestamp TIMESTAMPTZ NOT NULL,
    payload JSONB NOT NULL
);

CREATE INDEX idx_order_events_warehouse
ON order_events(warehouse_id);

CREATE INDEX idx_order_events_order
ON order_events(order_id);

CREATE INDEX idx_order_events_timestamp
ON order_events(event_timestamp);


-- -----------------------------------------------------
-- warehouse_metrics
-- Spark aggregations for dashboards
-- -----------------------------------------------------

CREATE TABLE warehouse_metrics (
    id BIGSERIAL PRIMARY KEY,

    warehouse_id VARCHAR(50) NOT NULL,

    window_start TIMESTAMPTZ NOT NULL,
    window_end TIMESTAMPTZ NOT NULL,

    total_orders INTEGER NOT NULL,
    total_revenue NUMERIC(12,2) NOT NULL,
    average_order_value NUMERIC(12,2) NOT NULL,

    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),

    UNIQUE (warehouse_id, window_start)
);

CREATE INDEX idx_warehouse_metrics_warehouse
ON warehouse_metrics(warehouse_id);

CREATE INDEX idx_warehouse_metrics_window_start
ON warehouse_metrics(window_start);


-- -----------------------------------------------------
-- anomalies
-- Operational alerts detected by Spark
-- -----------------------------------------------------

CREATE TABLE anomalies (
    anomaly_id BIGSERIAL PRIMARY KEY,

    warehouse_id VARCHAR(50) NOT NULL,

    anomaly_type VARCHAR(100) NOT NULL,
    severity VARCHAR(20) NOT NULL,

    description TEXT NOT NULL,

    detected_at TIMESTAMPTZ NOT NULL,

    estimated_impact NUMERIC(12,2) NOT NULL
);

CREATE INDEX idx_anomalies_warehouse
ON anomalies(warehouse_id);

CREATE INDEX idx_anomalies_detected_at
ON anomalies(detected_at);

CREATE INDEX idx_anomalies_severity
ON anomalies(severity);


-- -----------------------------------------------------
-- inventory_state
-- Current inventory snapshot
-- -----------------------------------------------------

CREATE TABLE inventory_state (
    warehouse_id VARCHAR(50) NOT NULL,
    sku_id VARCHAR(50) NOT NULL,

    available_quantity INTEGER NOT NULL,

    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),

    PRIMARY KEY (warehouse_id, sku_id)
);

CREATE INDEX idx_inventory_state_sku
ON inventory_state(sku_id);

CREATE INDEX idx_inventory_state_updated_at
ON inventory_state(updated_at);
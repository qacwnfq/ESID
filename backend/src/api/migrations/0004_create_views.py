# Generated by Django 3.2.3 on 2022-03-07 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_dataentry_percentile'),
    ]

    operations = [
        migrations.RunSQL(
            sql = "CREATE VIEW api_simulationdata AS \
                SELECT  \
                    api_dataentry.id as id , \
                    api_simulationnode_data.simulationnode_id as simulationnode_id, \
                    api_node.id as node_id, \
                    api_node.name as node_name, \
                    api_group.name as group, \
                    api_dataentry.day as day, \
                    api_dataentry.percentile as percentile, \
                    api_dataentry.data as data \
                FROM api_dataentry   \
                INNER JOIN api_simulationnode_data \
                    ON (api_dataentry.id = api_simulationnode_data.dataentry_id) \
                INNER JOIN api_simulationnode \
                    ON (api_simulationnode.id = api_simulationnode_data.simulationnode_id) \
                INNER JOIN api_scenarionode \
                    ON (api_scenarionode.id = api_simulationnode.scenario_node_id) \
                INNER JOIN api_node \
                    ON (api_node.id = api_scenarionode.node_id) \
                INNER JOIN api_group \
                    ON (api_dataentry.group_id = api_group.id) \
                ORDER BY api_dataentry.day ASC;",

            reverse_sql = "DROP VIEW IF EXISTS api_simulationdata"
        ),

        migrations.RunSQL(
            sql = "CREATE VIEW api_rkidata AS \
                SELECT  \
                    api_dataentry.id as id , \
                    api_rkinode_data.rkinode_id as rkinode_id, \
                    api_node.id as node_id, \
                    api_node.name as node_name, \
                    api_group.name as group, \
                    api_dataentry.day as day, \
                    api_dataentry.percentile as percentile, \
                    api_dataentry.data as data \
                FROM api_dataentry   \
                INNER JOIN api_rkinode_data \
                    ON (api_dataentry.id = api_rkinode_data.dataentry_id) \
                INNER JOIN api_rkinode \
                    ON (api_rkinode.id = api_rkinode_data.rkinode_id) \
                INNER JOIN api_node \
                    ON (api_node.id = api_rkinode.node_id) \
                INNER JOIN api_group \
                    ON (api_dataentry.group_id = api_group.id) \
                ORDER BY api_dataentry.day ASC;",

            reverse_sql = "DROP VIEW IF EXISTS api_rkidata"
        )

        
    ]

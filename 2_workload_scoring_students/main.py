import lib_main
import pandas as pd

DataFrame = lib_main.getFreshData(lib_main.CREDENTIALS,'findcsystem')
DataFrame = DataFrame.fillna('None')

users = DataFrame['assignee_id'].unique()
total_scores_table = pd.DataFrame()
status_scores_table = pd.DataFrame()

for user in users:
    workloadScores = workloadScoringByStatusesAndChannels(DataFrame[DataFrame.assignee_id == user][:],63,7)
    status_scores_table = pd.concat([status_scores_table, workloadScores])
    total_scores_table = pd.concat([total_scores_table, get_total_score(workloadScores)])

status_scores_table['assignee_id'] = status_scores_table['assignee_id'].astype('int64')
status_scores_table['status'] = status_scores_table['status'].astype('str')
status_scores_table['channel'] = status_scores_table['channel'].astype('str')
status_scores_table['count_last_period'] = status_scores_table['count_last_period'].astype('int32')
status_scores_table['count_mean_calc_period'] = status_scores_table['count_mean_calc_period'].astype('float')
status_scores_table['count_sem_calc_period'] = status_scores_table['count_sem_calc_period'].astype('float')
status_scores_table['score_value'] = status_scores_table['score_value'].astype('int32')

lib_main.insertScoreResultData(status_scores_table,'findcsystem','xsolla_summer_school','score_result_status_channel')

total_scores_table['assignee_id'] = total_scores_table['assignee_id'].astype('int64')

lib_main.insertScoreResultData(total_scores_table,'findcsystem','xsolla_summer_school','score_result_total')

import calendar
import pandas as pd
import plotly.graph_objects as go


def f(x):
  x = x.groupby(x['purchase_date'].dt.month)['product_name'].count()
  x.index = (x.index - 7) % 12
  x = x.sort_index().cumsum()
  x.index = [calendar.month_abbr[x] if x != 0 else calendar.month_abbr[12] for x in ((x.index + 7) % 12)]
  return x

def filter_dates(x, left : str, right : str):
  return x[(x['purchase_date'] >= left) & (x['purchase_date'] < right)]

if __name__ == '__main__':
	df2 = pd.read_csv(f"test_data/anonymised_membership_purchases.csv")
	df2['purchase_date'] = pd.to_datetime(df2['purchase_date'])

	membership_purchases = df2.loc[df2['product_name'].apply(lambda x: x.find('Membership') != -1)]
	daily_membership_2020 = f(filter_dates(membership_purchases, "2020-07-01", "2021-07-01"))
	daily_membership_2019 = f(filter_dates(membership_purchases, "2019-07-01", "2020-07-01"))
	daily_membership_2018 = f(filter_dates(membership_purchases, "2018-07-01", "2019-07-01"))
	daily_membership_2017 = f(filter_dates(membership_purchases, "2017-07-01", "2018-07-01"))

	membership_purchases_month_year = pd.DataFrame([daily_membership_2020,daily_membership_2019, daily_membership_2018, daily_membership_2017]).transpose()
	membership_purchases_month_year.columns=[2020, 2019, 2018, 2017]
	membership_purchases_month_year = membership_purchases_month_year.fillna(method='ffill')
	membership_purchases_month_year = membership_purchases_month_year.fillna(0)


	fig = go.Figure(go.Scatter(x=daily_membership_2020.index, y= daily_membership_2020.values, name="2020"))
	fig.add_trace(go.Scatter(x=daily_membership_2019.index, y= daily_membership_2019.values, name="2019"))
	fig.add_trace(go.Scatter(x=daily_membership_2018.index, y= daily_membership_2018.values, name="2018"))
	fig.add_trace(go.Scatter(x=daily_membership_2017.index, y= daily_membership_2017.values, name="2017"))
	fig.update_layout(title="Membership growth by year, month")
	fig.show()

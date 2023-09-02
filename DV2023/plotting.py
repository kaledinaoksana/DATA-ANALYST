import matplotlib.pyplot as plt
import pandas as pd
import setting as st

def plot_bar_month(values):

    data = {'Date': st.st.dates,
            'Issued': values}

    df = pd.DataFrame(data)
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    df['Issued_Diff'] = df['Issued'].diff()

    max_diff = df['Issued_Diff'].max()
    df = df[df['Issued_Diff'] != max_diff]

    df_monthly = df.resample('M').sum()

    monthly_average = df_monthly['Issued_Diff'].mean()

    plt.figure(figsize=(9, 6))
    ax = df_monthly['Issued_Diff'].plot(kind='bar', color='b', alpha=0.7)
    plt.axhline(y=monthly_average, color='r', linestyle='--', label='Monthly Average')

    plt.xticks(rotation=45)
    xtick_labels = [f"{month}" for month in df_monthly.index.strftime('%B')]
    ax.set_xticklabels(xtick_labels, rotation=45, ha='right')

    plt.xlabel('Month')
    plt.ylabel('Difference in Issued')
    plt.title('Difference in Issued Visas Between Consecutive Months with Monthly Average Line')

    plt.legend()

    plt.tight_layout()
    plt.show()



def plot_bar_week(data):
        df = pd.DataFrame(data)

        df['Date'] = pd.to_datetime(df['Date'])
        df.set_index('Date', inplace=True)

        df['Issued_Diff'] = df['Issued'].diff()
        df_weekly = df.resample('W').sum()

        weekly_average = df_weekly['Issued_Diff'].mean()

        plt.figure(figsize=(9, 6))
        ax = df_weekly['Issued_Diff'].plot(kind='bar', color='b', alpha=0.7)
        plt.axhline(y=weekly_average, color='r', linestyle='--', label='Weekly Average')

        xtick_labels = [f"{month} - Week {week}" for month, week in zip(df_weekly.index.strftime('%B'), df_weekly.index.isocalendar().week)]
        ax.set_xticklabels(xtick_labels, rotation=45, ha='right')

        plt.xlabel('Month and Week')
        plt.ylabel('Difference in Issued')
        plt.title('Difference in Issued Visas Between Consecutive Weeks with Weekly Average Line')

        plt.legend()

        plt.tight_layout()
        plt.show()


    
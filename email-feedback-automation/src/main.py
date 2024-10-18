from email_reader import fetch_emails
from sentiment_analysis import analyze_sentiment
from data_extractor import extract_data
from google_form_automation import submit_to_form
from notification_sender import send_notification

def main():
    # Step 1: Fetch Email Content
    email_content = fetch_emails()

    # Step 2: Analyze Sentiment
    sentiment, score = analyze_sentiment(email_content)

    # Step 3: Extract Data using TruCap+
    extracted_data = extract_data(email_content)
    extracted_data["SentimentScore"] = score
    extracted_data["Sentiment"] = sentiment

    # Step 4: Submit Data to Google Form
    submit_to_form(extracted_data)

    # Step 5: Send Notification Email
    summary = f"Sentiment: {sentiment}\nScore: {score}\nDetails: {extracted_data}"
    send_notification("Customer Feedback Summary", summary)

if __name__ == "__main__":
    main()

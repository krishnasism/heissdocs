from .engine import SummaryEngine


def summarize_text(body):
    summary_engine = SummaryEngine()
    summarized_body = {}
    for page_num, text in body.items():
        try:
            summarized_body[page_num] = " ".join(summary_engine.summarize(text))
        except:
            summarized_body[page_num] = text
    return summarized_body

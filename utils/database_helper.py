import sqlite3


def save_result(filename, role, score, matched, missing):

    conn = sqlite3.connect("resume.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO resume_history
        (filename, role, score, matched, missing)

        VALUES (?, ?, ?, ?, ?)
        """,
        (
            filename,
            role,
            score,
            ", ".join(matched),
            ", ".join(missing)
        )
    )

    conn.commit()

    conn.close()
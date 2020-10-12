from datetime import datetime, timedelta
from data.scoreboard_config import ScoreboardConfig
from renderers.main import MainRenderer
from renderers.offday import OffdayRenderer
from renderers.standings import StandingsRenderer
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from utils import args, led_matrix_options
from data.data import Data
import renderers.standings
import mlbgame
import debug

SCRIPT_NAME = "MLB LED Scoreboard"
SCRIPT_VERSION = "4.0.0"

# Get supplied command line arguments
args = args()

# Check for led configuration arguments
matrixOptions = led_matrix_options(args)

# Initialize the matrix
matrix = RGBMatrix(options = matrixOptions)

# Print some basic info on startup
debug.info("{} - v{} ({}x{})".format(SCRIPT_NAME, SCRIPT_VERSION, matrix.width, matrix.height))

# Read scoreboard options from config.json if it exists
config = ScoreboardConfig("config", matrix.width, matrix.height)
debug.set_debug_status(config)

# Create a new data object to manage the MLB data
# This will fetch initial data from MLB
data = Data(config)


while True:
    if datetime.now().strftime('%H') >= 07:    #Loop runs after 7AM.
        MainRenderer(matrix, data).render()
    elif datetime.now().strftime('%H') <= 19:    #Loop before 7PM.
        MainRenderer(matrix, data).render()
    else:
        break
#MainRenderer(matrix, data).render()

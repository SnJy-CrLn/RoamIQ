
function MainArea() {
  return (
    <main className="relative flex-1 min-h-screen bg-[url('/MainArea-BG.png')] bg-cover bg-center">

      {/* Background overlay */}
      <div className="absolute inset-0 bg-background/30" />

      {/* Main content */}
      <div className="relative z-10">
        MainArea
      </div>

    </main>
  );
}

export default MainArea;
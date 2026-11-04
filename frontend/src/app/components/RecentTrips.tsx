import { MessagesSquare } from 'lucide-react'
type RecentTripCardProps = {
    name: string,
    date: string
}
function RecentTrips() {
    const tripList = [
      { id: 1, name: "A trip to Goa for 4 days", date: "Today" },
      { id: 2, name: "Budget trip to Ooty", date: "Yesterday" },
      { id: 3, name: "Bali vacation", date: "Oct 29" },
    ];
    function RecentTripCard({name,date}: RecentTripCardProps){
        return(
            <div className='flex gap-2 items-center w-full h-13 hover:bg-card rounded-lg px-2 transition-colors cursor-pointer'>
               <MessagesSquare />
               {name}
               <p className='text-sm text-gray-500 ml-auto'>{date}</p> 
            </div>
        )
    }
  return (
    <div>
        <p className='text-[#8997ae] font-semibold'>Recent Trips</p>
        {
            tripList.map((trip)=>(
                <RecentTripCard key={trip.id} name={trip.name} date={trip.date}/>
            ))
        }
    </div>
  )
}

export default RecentTrips